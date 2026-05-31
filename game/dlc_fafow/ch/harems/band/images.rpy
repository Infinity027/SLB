init 1:
    layeredimage band threesome fuckamy:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, MCCGPicker], npcs=[amy, sasha], add_simple_outfit_attribute=True)

        attribute mikemc null
        attribute amy null
        attribute sasha null
        attribute casual null

        always "band_threesome_fuckamy_bg"

        always "band_threesome_fuckamy_bodies"

        group haircuts auto

        attribute amy_nohaircut null

        group multiple auto variant pregnancies

        attribute sasha_boobjob
        attribute sasha_noboobjob null

        group multiple auto variant piercings
        group multiple:
            attribute amy_nipples null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute sasha_lips null
            attribute sasha_nose null
            attribute sasha_tongue null
        group piercings auto variant "boobjob" if_any "sasha_boobjob"
        group piercings auto variant "noboobjob" if_any "sasha_noboobjob"

        attribute naked null
        attribute amy_naked null
        attribute sasha_naked null

        group multiple auto variant outfits when not naked
        group outfits auto variant "amy_pregnant" if_any "amy_pregnant" if_not "naked"
        group outfits auto variant "sasha_pregnant" if_any "sasha_pregnant" if_not "naked"
        group outfits auto variant "boobjob" if_any "sasha_boobjob" if_not "naked"

        group multiple auto variant collars

        group mcoutfits auto:
            attribute mc_naked null

        group dick_location:
            attribute out null default
            attribute vaginal null

        group dick auto variant "out" if_any "out"
        group dick auto variant "vaginal" if_any "vaginal"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute wet

    layeredimage band threesome fucksasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, MCCGPicker], npcs=[amy, sasha], add_simple_outfit_attribute=True)

        attribute mikemc null
        attribute amy null
        attribute sasha null
        attribute casual null

        always "band_threesome_fucksasha_bg"

        always "band_threesome_fucksasha_bodies"

        group mcoutfits auto:
            attribute mc_naked null

        group haircuts auto

        attribute amy_nohaircut null

        group multiple auto variant pregnancies

        attribute sasha_boobjob
        attribute sasha_noboobjob null

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute amy_nipples null
            attribute amy_nose null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_tongue null
        group piercings auto variant "boobjob" if_all ["sasha_boobjob", "naked"]
        group piercings auto variant "noboobjob" if_all ["sasha_noboobjob", "naked"]

        attribute naked null
        attribute amy_naked null
        attribute sasha_naked null

        group multiple auto variant outfits when not naked
        group outfits auto variant "amy_pregnant" if_any "amy_pregnant" if_not "naked"
        group outfits auto variant "sasha_pregnant" if_any "sasha_pregnant" if_not "naked"
        group outfits auto variant "boobjob" if_any "sasha_boobjob" if_not "naked"

        group multiple auto variant collars
        group multiple:
            attribute sasha_collar null



        group dick_location:
            attribute out null default
            attribute vaginal null

        group dick auto variant "out" if_any "out"
        group dick auto variant "vaginal" if_any "vaginal"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute wet

    layeredimage ferris lookout amysasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, MCCGPicker], npcs=[amy, sasha], add_simple_outfit_attribute=True)

        attribute naked null
        attribute amy_naked null
        attribute sasha_naked null
        attribute mc_naked null

        attribute amy_nohaircut null
        attribute casual null
        attribute mc_casual null
        group dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_big null


        always "ferris_lookout_amysasha_bg"

        attribute mikemc

        group exp auto:
            attribute normal default

        always "ferris_lookout_amysasha_back_mc_casual" if_not "naked"

        group multiple auto variant npcs

        attribute sasha_pregnant

        group multiple auto variant collars

        group boobjobs auto:
            attribute sasha_noboobjob null

        group multiple auto variant piercings_hidden
        group piercings_boobjob auto if_any "sasha_boobjob"
        group piercings_noboobjob auto if_any "sasha_noboobjob"

        group multiple auto variant outfits when not naked

        attribute amy_pregnant

        group outfits_sasha_pregnant auto if_any "sasha_pregnant" if_not "naked"
        group outfits_boobjob auto if_any "sasha_boobjob" if_not "naked"
        group outfits_amy_pregnant auto if_any "amy_pregnant" if_not "naked"

        group multiple auto variant piercings
        group multiple:
            attribute sasha_lips null

        group haircuts auto

        always "ferris_lookout_amysasha_legs_mikemc"
        always "ferris_lookout_amysasha_front_mc_casual" if_not "naked"


    layeredimage band handjob amysasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, OutfitPicker, MCCGPicker], npcs=[amy, sasha], add_simple_outfit_attribute=True)

        attribute naked null
        attribute amy_naked null
        attribute sasha_naked null
        attribute mc_naked null

        attribute amy_nohaircut null
        attribute casual null
        attribute mc_casual null

        always "band_handjob_amysasha_bg"

        attribute mikemc

        group exp auto:
            attribute normal default


        always "band_handjob_amysasha_back_mc_casual" if_not "naked"

        group multiple auto variant npcs

        attribute sasha_pregnant

        group multiple auto variant collars

        group boobjobs auto:
            attribute sasha_noboobjob null

        group multiple auto variant piercings_hidden
        group piercings_boobjob auto if_any "sasha_boobjob"
        group piercings_noboobjob auto if_any "sasha_noboobjob"

        group multiple auto variant outfits when not naked

        attribute amy_pregnant

        group outfits_sasha_pregnant auto if_any "sasha_pregnant" if_not "naked"
        group outfits_boobjob auto if_any "sasha_boobjob" if_not "naked"
        group outfits_amy_pregnant auto if_any "amy_pregnant" if_not "naked"

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_pregnant_navel null
            attribute sasha_lips null
            attribute sasha_nipples null
            attribute sasha_tongue null

        group haircuts auto

        always "band_handjob_amysasha_legs_mikemc"
        always "band_handjob_amysasha_front_mc_casual" if_not "naked"

        group dicks auto

        group sasha_hand auto
        group amy_hand auto

        attribute cumshot null
        group cumshot auto if_any "cumshot"


    layeredimage band blowjob amykleio:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, MCCGPicker], npcs=[amy, kleio])


        attribute mc_casual null
        attribute mc_date null

        group bg auto:
            attribute bedroom default

        attribute mikemc

        group leftarm auto:
            attribute lefthold default

        group rightarm auto:
            attribute righthold default

        group dicks auto:
            attribute outside null default
            attribute amysuck
            attribute kleiosuck

        group dicks auto variant "outside" if_any "outside"

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        group cumshot auto variant "mc" if_any "cumshot" if_not ["amysuck", "kleiosuck"]

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        attribute insert null
        group insert_bg auto if_any "insert"
        group insert_haircuts auto if_any "insert"
        group insert_cumshot auto if_all ["insert", "cumshot"]

        attribute amy_nohaircut null
        group amy auto:
            attribute amysuck null
            attribute amylick null

        attribute amy_collar null

        group kleio auto:
            attribute kleiosuck null
            attribute kleiolick null

        attribute kleio_collar null

        group multiple auto variant tongue

        group multiple auto variant heads

        group kleioeyes auto:
            attribute normal default

        group tattoos auto

        group multiple auto variant backs

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute amy_nipples null
            attribute amy_nose null
            attribute kleio_clit null
            attribute kleio_ears null
            attribute kleio_navel null
            attribute kleio_pregnant_navel null
            attribute kleio_nipples null
            attribute kleio_nose null
            attribute kleio_tongue null

        group multiple auto variant vibrators
        group multiple auto variant fx

        group amyplug auto
        group kleioplug auto

        group lefthand auto
        group righthand auto

        group fg auto


    layeredimage band threesome amykleio fuckamy:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, MCCGPicker], npcs=[amy, kleio])

        attribute nomc null
        attribute mikemc null

        group bg auto:
            attribute bedroom default

        attribute insert null
        group multiple auto variant insert_bg when insert
        group insert_condom auto if_all ["insert", "condom"]
        group insert_creampie auto if_all ["insert", "creampie"]
        attribute squirt null
        group insert_squirt auto if_all ["insert", "squirt"]

        always "band_threesome_amykleio_fuckamy_amy_leg"

        always:
            if_not "nomc"
            "band_threesome_amykleio_fuckamy_mike_back"

        group dicks auto if_not "nomc":
            attribute outside null default
            attribute vaginal
            attribute anal

        group dicks auto variant "outside" if_any "outside" if_not "nomc"

        attribute condom null
        group condom auto if_any "condom" if_not "nomc"
        group condom auto variant "outside" if_all ["outside", "condom"] if_not "nomc"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "nomc"

        attribute creampie null
        group creampie auto if_any "creampie" if_not "nomc"

        attribute amy null
        attribute kleio null
        always "band_threesome_amykleio_fuckamy_bodies"

        always "band_threesome_amykleio_fuckamy_mike_hand" if_not "nomc"

        group multiple auto variant pregnancies

        attribute amy_nohaircut null
        attribute kleio_nohaircut null
        attribute kleio_haircut

        group tattoos auto:
            attribute kleio_angel null
            attribute kleio_wolf null

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute kleio_clit null
            attribute kleio_ears null
            attribute kleio_navel null
            attribute kleio_pregnant_navel null
            attribute kleio_tongue null

        group multiple auto variant collars

        always "band_threesome_amykleio_fuckamy_mike_head" if_not "nomc"

        group kleio_hand auto:
            attribute onamy default

        group fg auto

    layeredimage band threesome amykleio fuckkleio:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, HaircutPicker, MCCGPicker], npcs=[amy, kleio])

        attribute nomc null
        attribute mikemc null

        attribute mc_casual null
        attribute mc_date null

        group bg auto:
            attribute bedroom default

        attribute amy null
        attribute kleio null
        always "band_threesome_amykleio_fuckkleio_head_amy"
        always "band_threesome_amykleio_fuckkleio_head_kleio"

        group amyeyes auto:
            attribute amyopen default
        group amymouth auto:
            attribute amynormal default

        group kleioeyes auto:
            attribute kleioopen default
        group kleiomouth auto:
            attribute kleionormal default

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute amy_nipples null
            attribute kleio_clit null
            attribute kleio_navel null
            attribute kleio_pregnant_navel null
            attribute kleio_nipples null
            attribute kleio_tongue null

        attribute amy_collar null
        attribute kleio_collar null

        attribute amy_nohaircut null
        group haircuts auto

        attribute amy_pregnant null
        attribute kleio_pregnant null

        always "band_threesome_amykleio_fuckkleio_bodies"

        group tattoos auto

        attribute kleio_plug
        attribute amy_plug

        group dicks auto if_not "nomc"
        group mikemc auto if_not "nomc":
            attribute outside default

        group dicks auto variant "outside" if_any "outside" if_not "nomc"

        attribute condom null
        group condom auto if_any "condom" if_not "nomc"
        group condom auto variant "outside" if_all ["outside", "condom"] if_not "nomc"

        attribute creampie null
        group creampie auto if_any "creampie" if_not "nomc"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "nomc"

        attribute cum null
        group multiple auto variant cum when cum and not nomc

        group fg auto

    layeredimage band foreplay amyanna:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, MCCGPicker], npcs=[amy, anna])

        attribute nomc null
        attribute mikemc null
        attribute amy null
        attribute anna null

        attribute mc_casual null
        attribute mc_date null

        attribute inside null

        group bg auto:
            attribute bedroom default

        always "band_foreplay_amyanna_bodies"


        always "band_foreplay_amyanna_mike_exp"

        attribute amy_blush
        attribute anna_blush

        group amy_exp auto:
            attribute ameyes_closed default

        group anna_exp auto:
            attribute aneyes_closed default


        group dick auto if_not "inside"

        attribute cum null
        group cum auto if_any "cum" if_not "inside"


        group anna_rarm auto:
            attribute face default
            attribute handjob if_not "inside"
        always "band_foreplay_amyanna_anna_elbow" if_any "handjob" if_not "inside"


        group multiple auto variant pregnancies


        group multiple auto variant piercings
        group multiple:
            attribute anna_clit null
            attribute anna_ears null


        group anna_larm auto:
            attribute front default

        group multiple auto variant collars

        group multiple auto variant fx

    layeredimage band threesome amyanna fuckanna:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, PubesPicker, MCCGPicker], npcs=[amy, anna])

        attribute amy null
        attribute anna null
        attribute mikemc null

        attribute mc_casual null

        group bg auto:
            attribute bedroom default

        always "band_threesome_amyanna_fuckanna_bodies"

        attribute amy_pubes null
        attribute anna_pubes

        group multiple auto variant pregnancies

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute anna_ears null
            attribute anna_tongue null

        group piercings auto variant "vaginal" if_any "vaginal"
        group piercings auto variant "anal" if_any "anal"

        group multiple auto variant collars

        group amy_mouth auto:
            attribute amy_normal default

        group anna_mouth auto:
            attribute anna_normal default

        group anna_eyes auto

        group tits auto:
            attribute still default

        group piercings auto variant "still" if_any "still"
        group piercings auto variant "bouncing1" if_any "bouncing1"
        group piercings auto variant "bouncing2" if_any "bouncing2"

        group dick auto:
            attribute outside null default
            attribute anal
            attribute vaginal

        group dick auto variant "outside" if_any "outside"

        attribute condom null
        group condom auto if_any "condom"
        group condom auto variant "outside" if_all ["outside", "condom"]

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "condom"

        attribute creampie null
        group creampie auto if_any "creampie" if_not "condom"

        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not "condom"

        always "band_threesome_amyanna_fuckanna_mikemc_hand"
        group fg auto


    layeredimage band threesome amyanna fuckamy:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, MCCGPicker], npcs=[amy, anna])

        attribute amy null
        attribute anna null
        attribute nomc null

        attribute mc_casual null

        group bg auto:
            attribute bedroom default

        attribute insert null
        group insert_bg auto if_any "insert" if_not "nomc"
        group insert_condom auto if_all ["insert", "condom"] if_not "nomc"
        group insert_creampie auto if_all ["insert", "creampie"] if_not "nomc"

        attribute mikemc if_not "nomc"
        group dick auto:
            attribute outside null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "outside" if_any "outside" if_not "nomc"

        always "band_threesome_amyanna_fuckamy_bodies"

        group multiple auto variant pregnancies

        group multiple auto variant piercings
        group multiple:
            attribute amy_clit null
            attribute amy_ears null
            attribute amy_navel null
            attribute amy_pregnant_navel null
            attribute amy_nipples null
            attribute anna_clit null
            attribute anna_ears null
            attribute anna_navel null
            attribute anna_pregnant_navel null
            attribute anna_tongue null

        group multiple auto variant collars

        group eyes auto:
            attribute onanna default

        attribute condom null
        group condom auto variant "outside" if_all ["outside", "condom"] if_not "nomc"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "nomc"

        attribute creampie null

        attribute cum null
        group cum auto if_any "cum" if_not "nomc"

        always "band_threesome_amyanna_fuckamy_mike_hands" if_not "nomc"

        group fg auto


    layeredimage fivesome amyannakleiosasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, PiercingsPicker, PubesPicker, HaircutPicker, MCCGPicker], npcs=[amy, anna, kleio, sasha])

        attribute mikemc null
        attribute mc_casual null

        always "fivesome_amyannakleiosasha_bg"
        always "fivesome_amyannakleiosasha_shade"


        attribute nokleiosasha null
        always "fivesome_amyannakleiosasha_kleio_sasha" if_not "nokleiosasha"

        attribute kleio null
        group multiple auto variant kleio_piercings when not nokleiosasha:
            attribute kleio_clit null
            attribute kleio_nipples null
            attribute kleio_navel null
            attribute kleio_pregnant_navel null
            attribute kleio_tongue null
        attribute kleio_collar if_not "nokleiosasha"
        attribute kleio_pregnant if_not "nokleiosasha"
        attribute kleio_pubes null
        attribute kleio_nohaircut null
        attribute kleio_haircut if_not "nokleiosasha"
        group tattoo auto if_not "nokleiosasha"

        attribute sasha null
        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        group multiple auto variant sasha_piercings when not nokleiosasha:
            attribute sasha_clit null
            attribute sasha_ears null
            attribute sasha_lips null
            attribute sasha_nipples null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_nose null
            attribute sasha_tongue null
        attribute sasha_collar if_not "nokleiosasha"
        attribute sasha_pregnant if_not "nokleiosasha"
        attribute sasha_nohaircut if_not "nokleiosasha"
        attribute sasha_haircut null

        attribute amy
        group multiple auto variant amy_piercings
        group multiple:
            attribute amy_clit null
            attribute amy_navel null
            attribute amy_pregnant_navel null
        attribute amy_collar
        attribute amy_pregnant null

        attribute noanna null
        attribute anna if_not "noanna"
        group multiple auto variant anna_piercings when not noanna:
            attribute anna_ears null
            attribute anna_tongue null
        attribute anna_collar if_not "noanna"
        attribute anna_pubes if_not "noanna"
        attribute anna_pregnant if_not "noanna"

        group dick auto:
            attribute outside null default
            attribute vaginal
            attribute anal

        group dick auto variant "outside" if_any "outside"

        group anna_arm auto if_not "noanna":
            attribute balls default

        attribute condom null
        group condom auto if_any "condom"
        group condom auto variant "outside" if_all ["condom", "outside"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie"

        group eyes auto:
            attribute opened default

        group mouth auto:
            attribute normal default

    layeredimage band amy ending:
        attribute_function MultiPickers([HaircutPicker, EndingKidPicker], npcs=[amy, anna, kleio, sasha])

        always "band_amy_ending_bg"

        always "band_amy_ending_right_picture_frame"

        attribute kleio
        attribute sasha
        attribute sasha_boobjob

        group multiple auto variant haircuts

        always "band_amy_ending_right_picture_couch"

        always "band_amy_ending_mikemc"

        attribute amy
        attribute anna

        always "band_amy_ending_left_picture_frame" when amy_kid or anna_kid or kleio_kid or sasha_kid
        group multiple auto variant kids

        always "band_amy_ending_trophy"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
