init 1:
    layeredimage reona smartphone:
        always "reona_smartphone"

    layeredimage reona kiss:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker, HaircutPicker, MCCGPicker], npc=reona)

        attribute reona null
        attribute mikemc null

        group dick auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group wings auto


        group bodies auto




        attribute collar


        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute nipples null
            attribute tongue null
            attribute navel null
            attribute pregnant_navel null


        attribute naked null
        attribute topless null
        attribute innersexy null
        group inneroutfit auto when not (innersexy or naked or topless)
        group inneroutfit auto variant sexy when innersexy and not (naked or topless)
        group outfit auto when not naked


        attribute mc_naked null
        group mikeoutfit auto if_not ["mc_naked"]

        attribute glasses
        attribute pureglasses


    layeredimage reona kiss jack:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, OutfitPicker, PregnancyPicker], npcs=[jack, reona], add_simple_outfit_attribute=True)

        attribute reona null
        attribute jack null

        group wings auto


        always "reona_kiss_jack_bodies"

        group eyes auto

        attribute reona_pregnant


        attribute reona_collar


        group multiple auto variant piercings
        group multiple:
            attribute reona_clit null
            attribute reona_tongue null
            attribute reona_navel null
            attribute reona_pregnant_navel null


        attribute jack_naked null
        group jackoutfit auto if_not ["naked", "jack_naked"]


        attribute reona_naked null
        group outfit auto if_not ["naked", "reona_naked"]

        group multiple:
            attribute naked null
            attribute casual null
            attribute date null
            attribute halloween null
            attribute purecasual null
            attribute puredate null
            attribute sexydate null
            attribute sexyswimsuit null
            attribute sport null
            attribute swimsuit null
            attribute underwear null
            attribute wedding null

        attribute pureglasses

        group haircuts auto

        group acc auto variant "nohaircut" if_any "reona_nohaircut"
        group acc auto variant "haircut" if_any "reona_haircut"


    layeredimage reona cunnilingus:
        attribute_function Pickers([MCCGPicker, OutfitPicker, PubesPicker, PregnancyPicker, PiercingsPicker], npc=reona)


        group bg auto:
            attribute bedroom default


        always "reona_cunnilingus_body"


        attribute pubes


        attribute pregnant


        group head auto:
            attribute down null default
            attribute up null

        group head auto variant "up" if_any "up"
        group head auto variant "down" if_any "down"


        group eyes auto:
            attribute eyes_open null default
            attribute eyes_ahegao null
            attribute eyes_close null
            attribute eyes_surprised null

        group mouth auto:
            attribute mouth_normal null default
            attribute mouth_ahegao null
            attribute mouth_hurt null
            attribute mouth_pleasure null

        group eyesdown auto variant "nohaircut" if_all ["down", "nohaircut"]
        group eyesdown auto variant "haircut" if_all ["down", "haircut"]
        group mouthdown auto if_any ["down"]
        group eyesup auto variant "nohaircut" if_all ["up", "nohaircut"]
        group eyesup auto variant "haircut" if_all ["up", "haircut"]
        group mouthup auto if_any ["up"]

        group glasses auto variant "up" if_any "up"
        group glasses auto variant "down" if_any "down"


        attribute topless null
        attribute bottomless null
        attribute naked null
        group top auto if_not ["topless", "naked"]
        group top auto variant "pregnant" if_not ["topless", "naked"] if_any "pregnant"
        group bot auto if_not ["bottomless", "naked"]


        attribute collar

        group inreo:
            attribute finger null
            attribute beads null
            attribute dildo null
            attribute mike null


        group finger auto if_any ["finger"]:
            attribute tip default


        group beads auto if_any ["beads"]:
            attribute beads_1 default


        group dildo auto if_any ["dildo"]:
            attribute tip default


        attribute mikemc null
        attribute mike
        attribute mc_casual if_any ["mike"]

        group dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group multiple auto variant piercings
        group multiple:
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        group multiple auto variant piercings_notop when (topless or naked)
        group multiple auto variant piercings_dildo when dildo
        group multiple auto variant piercings_notdildo when not dildo


        attribute squirt

    layeredimage reona bj:
        attribute_function Pickers([PiercingsPicker, PubesPicker, CollarPicker, DickPicker], npc=reona)


        group bg auto:
            attribute bedroom default


        always "reona_bj_body"


        attribute pubes


        attribute collar


        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute tongue null


        group head_position auto:
            attribute down null default
            attribute up null
            attribute suck null

        group head auto variant "haircut" if_all "haircut"
        group head auto variant "nohaircut" if_all "nohaircut"


        group multiple auto variant piercings_down when down
        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_suck when suck


        group mouth auto variant "down" if_any ["down"]:
            attribute mouth_open default
        group mouth auto variant "up" if_any ["up"]:
            attribute mouth_open default


        attribute tongueout null
        group tongueout auto if_all ["tongueout", "mouth_open"] if_not ["suck"]


        attribute mouthcum null
        group mouthcum auto if_all ["mouthcum", "tongueout"] if_not ["suck"]


        group eyes_position auto:
            attribute eyes_open null default
            attribute eyes_close null
            attribute eyes_ahegao null
        group eyes auto variant "down_nohaircut" if_all ["down", "nohaircut"]
        group eyes auto variant "up_nohaircut" if_all ["up", "nohaircut"]
        group eyes auto variant "suck_nohaircut" if_all ["suck", "nohaircut"]
        group eyes auto variant "down_haircut" if_all ["down", "haircut"]
        group eyes auto variant "up_haircut" if_all ["up", "haircut"]
        group eyes auto variant "suck_haircut" if_all ["suck", "haircut"]

        group glasses auto variant "up" if_any "up"
        group glasses auto variant "down" if_any "down"
        group glasses auto variant "suck" if_any "suck"

        group hairs auto variant "up" if_any "up"
        group hairs auto variant "down" if_any "down"
        group hairs auto variant "suck" if_any "suck"


        attribute facecum null
        group facecum auto if_any ["facecum"]


        group dick if_any ["mike"]:
            attribute out default null
            attribute suck
            attribute handjob null
        group dick auto variant "out" if_all ["mike", "out"]
        group dick auto variant "handjob" if_all ["mike", "handjob"]


        group right:
            attribute cup
            attribute squeeze
            attribute rightpeace
        always "reona_bj_right_squeeze" if_not ["mike", "cup", "squeeze", "rightpeace"]


        attribute cum null
        group cum auto if_all ["mike", "cum"]
        attribute cupcum if_all ["mike", "cum", "cup"]


        group left if_not ["handjob"]:
            attribute finger
            attribute leftpeace
        always "reona_bj_left_handjob" if_all ["mike", "handjob"]
        always "reona_bj_left_finger" if_not ["mike", "finger", "leftpeace"]


        attribute dildo null
        group dildo auto if_any ["dildo"]:
            attribute vaginal default


        always "reona_bj_rightshoulder_hold" if_all ["mike"] if_not ["cup", "squeeze", "rightpeace"]
        always "reona_bj_leftshoulder_hold" if_all ["mike"] if_not ["handjob", "finger", "leftpeace"]


        attribute mike


        attribute squirt


        always "reona_bj_right_hold" if_all ["mike"] if_not ["cup", "squeeze", "rightpeace"]
        always "reona_bj_left_hold" if_all ["mike"] if_not ["handjob", "finger", "leftpeace"]

    layeredimage reona missionary:
        attribute_function Pickers([PubesPicker, CollarPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=reona)


        group bg auto:
            attribute bedroom default


        attribute mike null
        group mike auto if_any ["mike"]:
            attribute back default

        group reona auto


        always "reona_missionary_horns" if_any ["halloween"]


        attribute pubes
        attribute pregnant
        attribute collar
        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute tongue null


        group eyes auto:
            attribute eyes_open null default
            attribute eyes_ahegao null
            attribute eyes_close null
            attribute eyes_hurt null
            attribute eyes_surprised null

        group eyes auto variant "haircut" if_any "haircut"
        group eyes auto variant "nohaircut" if_any "nohaircut"

        group mouth auto:
            attribute mouth_normal default

        attribute pureglasses


        attribute analgape if_not ["analdrip", "buttplug", "anal"]
        always "reona_missionary_analgape" if_any ["buttplug"] if_not ["anal"]
        always "reona_missionary_analgape" if_any ["analdrip"] if_not ["buttplug", "anal"]
        attribute analdrip if_not ["buttplug", "anal"]
        attribute buttplug if_not ["anal"]


        attribute vaginalgape if_not ["vaginaldrip", "beads", "vaginal"]
        always "reona_missionary_vaginalgape" if_any ["vaginaldrip"] if_not ["beads", "vaginal"]
        always "reona_missionary_vaginalgape" if_all ["beads", "pulled", "mike"] if_not ["vaginal"]
        attribute vaginaldrip if_not ["beads", "vaginal"]
        attribute beads null if_not ["vaginal"]
        group beads if_any ["beads"] if_not ["vaginal"]:
            attribute normal default


        attribute speed if_any ["mike"]


        group dick_options:
            attribute out default null
            attribute vaginal null
            attribute anal null


        group dick auto variant "vaginal" if_all ["vaginal", "mike"]
        group dick auto variant "anal" if_all ["anal", "mike"]


        attribute condom null
        group condom auto variant "vaginal" if_all ["condom", "vaginal", "mike"]


        attribute cum null
        group cum auto variant "vaginal" if_all ["cum", "vaginal", "mike"] if_not ["condom"]
        group cum auto variant "anal" if_all ["cum", "anal", "mike"] if_not ["condom"]


        group beads if_all ["beads", "mike"] if_not ["vaginal"]:
            attribute normal default null
            attribute standby
            attribute pulled


        group multiple auto variant piercings_vaginal when vaginalgape or vaginaldrip or vaginal or beads


        attribute naked null
        group top auto if_not ["naked"]
        group bot auto if_not ["naked"]


        group righthand auto:
            attribute right_hold default
        group lefthand auto:
            attribute left_hold default


        group rightsleeve_halloween auto if_any ["halloween"] if_not ["naked"]
        group leftsleeve_halloween auto if_any ["halloween"] if_not ["naked"]


        attribute notail null
        always "reona_missionary_tail" if_any ["halloween"] if_not ["notail", "vaginal", "anal", "analdrip", "buttplug", "analgape"]


        group dick_out auto variant "back" if_all ["out", "back", "mike"]
        group dick_out auto variant "forth" if_all ["out", "forth", "mike"]


        group condom_out auto variant "back" if_all ["condom", "out", "back", "mike"] if_not ["cum"]
        group condom_out auto variant "forth" if_all ["condom", "out", "forth", "mike"] if_not ["cum"]
        group condom_cum auto variant "back" if_all ["condom", "cum", "back", "out", "mike"]
        group condom_cum auto variant "forth" if_all ["condom", "cum", "forth", "out", "mike"]


        group cum_out auto variant "back" if_all ["cum", "out", "back", "mike"] if_not ["condom"]
        group cum_out auto variant "forth" if_all ["cum", "out", "forth", "mike"] if_not ["condom"]


        always "reona_missionary_mikehand_left" if_any ["mike"]
        always "reona_missionary_mikehand_right" if_any ["mike"] if_not ["beads"]
        always "reona_missionary_mikehand_right" if_all ["mike"] if_any ["beads"] if_not ["standby", "pulled"]

    layeredimage reona cowgirl:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=reona)


        always "reona_cowgirl_bg"


        always "reona_cowgirl_bodies"


        attribute collar


        attribute pubes


        group eyes auto:
            attribute eyes_lookdown default
        group mouth auto:
            attribute mouth_normal default


        group dick auto:
            attribute out null default


        attribute condom null
        group condom auto if_any ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        attribute pregnant


        group multiple auto variant piercings
        group multiple auto variant piercings_vaginal when vaginal


        group dick auto variant "out" if_any ["out"]


        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]
        group condom auto variant "cum" if_all ["condom", "cum", "out"]


        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        group fg auto

    layeredimage reona reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, PubesPicker, PregnancyPicker], npc=reona)


        group bg auto:
            attribute cinema default


        always "reona_reverse_cowgirl_bodies_mikemc"
        always "reona_reverse_cowgirl_bodies_reona"


        attribute collar


        attribute pubes


        group eyes_positions auto:
            attribute eyes_lookdown null default
            attribute eyes_ahegao null
            attribute eyes_close null
            attribute eyes_open null

        group eyes auto variant "haircut" if_any "haircut"
        group eyes auto variant "nohaircut" if_any "nohaircut"

        always if_any "nohaircut":
            "reona_reverse_cowgirl_tattoo"

        attribute pureglasses

        group mouth auto:
            attribute mouth_normal default

        group haircuts auto


        group dick:
            attribute out null default
            attribute vaginal
            attribute anal


        attribute condom null
        group condom if_any ["condom"]:
            attribute vaginal


        attribute cum null
        group cum if_any ["cum"] if_not ["cum"]:
            attribute vaginal
            attribute anal


        attribute pregnant


        always "reona_reverse_cowgirl_mike_righthand1"
        always "reona_reverse_cowgirl_reona_righthand" if_not ["handjob"]


        group dick:
            attribute out null default
            attribute handjob
        group dick auto variant "out" if_any ["out"]


        always "reona_reverse_cowgirl_mike_righthand2"
        always "reona_reverse_cowgirl_reona_lefthand"
        always "reona_reverse_cowgirl_mike_lefthand"


        group multiple auto variant piercings
        group multiple:
            attribute tongue null
        group multiple auto variant piercings_vaginal when vaginal


        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]
        group condom auto variant "cum" if_all ["condom", "cum", "out"]


        group cum if_any ["cum"]:
            attribute handjob
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        group fg auto

    layeredimage reona doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, DickPicker], npc=reona)

        group smashed auto:
            attribute notsmash null default
            attribute smash null

        group pull auto:
            attribute notpulled null default
            attribute pulled null


        group bg auto:
            attribute bedroom default


        attribute mike null
        group mikehand auto if_any ["mike"]
        group mikehand auto variant "nohaircut" if_all ["mike", "nohaircut"]
        group mikehand auto variant "haircut" if_all ["mike", "haircut"]
        group mike_back auto if_any ["mike"]:
            attribute smash null


        group fuckpos:
            attribute out default null
            attribute vaginal null
            attribute anal null


        group dick auto if_all ["mike", "notsmash"]
        group dick auto variant "out" if_all ["mike", "out", "notsmash"]


        attribute cum null
        group cum auto variant "out" if_all ["mike", "out", "cum", "notsmash"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom", "notsmash"] if_not ["cum"]
        group condom auto variant "out" if_all ["mike", "out", "condom", "notsmash"] if_not ["cum"]
        group condomcum auto if_all ["mike", "out", "condom", "cum", "notsmash"]



        group fronthand auto


        group body auto:
            attribute rest null default
            attribute bounce null

        group body auto variant "notsmash" if_any ["notsmash"]
        group body auto variant "smash" if_any ["smash"]


        group lowerbody auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group head auto variant "notsmash_notpulled" if_all ["notsmash", "notpulled"]
        group head auto variant "notsmash_pulled" if_all ["notsmash", "pulled"]
        group head auto variant "smash_notpulled" if_all ["smash", "notpulled"]
        group head auto variant "smash_pulled" if_all ["smash", "pulled"]


        group collars auto variant "notsmash_notpulled_haircut" if_all ["notsmash", "notpulled", "haircut"]
        group collars auto variant "notsmash_notpulled_nohaircut" if_all ["notsmash", "notpulled", "nohaircut"]
        group collars auto variant "notsmash_pulled_haircut" if_all ["notsmash", "pulled", "haircut"]
        group collars auto variant "notsmash_pulled_nohaircut" if_all ["notsmash", "pulled", "nohaircut"]
        group collars auto variant "smash_notpulled_haircut" if_all ["smash", "notpulled", "haircut"]
        group collars auto variant "smash_notpulled_nohaircut" if_all ["smash", "notpulled", "nohaircut"]
        group collars auto variant "smash_pulled_haircut" if_all ["smash", "pulled", "haircut"]
        group collars auto variant "smash_pulled_nohaircut" if_all ["smash", "pulled", "nohaircut"]


        group reonamouth auto:
            attribute mouth_normal null default
            attribute mouth_ahegao null
            attribute mouth_pleasure null
            attribute mouth_teeth null

        group reonamouth auto variant "notsmash_notpulled" if_all ["notsmash", "notpulled"]
        group reonamouth auto variant "notsmash_pulled" if_all ["notsmash", "pulled"]
        group reonamouth auto variant "smash_pulled" if_all ["smash", "pulled"]
        group reonamouth auto variant "smash_notpulled" if_all ["smash", "notpulled"]


        group reonaeyes auto:
            attribute eyes_normal null default
            attribute eyes_ahegao null
            attribute eyes_closed null
            attribute eyes_pleasure null

        group reonaeyes auto variant "notsmash_notpulled_haircut" if_all ["notsmash", "notpulled", "haircut"]
        group reonaeyes auto variant "notsmash_notpulled_nohaircut" if_all ["notsmash", "notpulled", "nohaircut"]
        group reonaeyes auto variant "notsmash_pulled_haircut" if_all ["notsmash", "pulled", "haircut"]
        group reonaeyes auto variant "notsmash_pulled_nohaircut" if_all ["notsmash", "pulled", "nohaircut"]
        group reonaeyes auto variant "smash_pulled_haircut" if_all ["smash", "pulled", "haircut"]
        group reonaeyes auto variant "smash_pulled_nohaircut" if_all ["smash", "pulled", "nohaircut"]
        group reonaeyes auto variant "smash_notpulled_haircut" if_all ["smash", "notpulled", "haircut"]
        group reonaeyes auto variant "smash_notpulled_nohaircut" if_all ["smash", "notpulled", "nohaircut"]


        group backhand auto


        attribute naked null
        group underwear auto if_not "naked"



        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute tongue null


        group multiple auto variant piercings_notsmash when notsmash
        group multiple auto variant piercings_notsmash_rest when notsmash and rest
        group multiple auto variant piercings_notsmash_bounce when notsmash and bounce
        group multiple auto variant piercings_notsmash_notpulled when notsmash and notpulled
        group multiple auto variant piercings_notsmash_pulled when notsmash and pulled


        group multiple auto variant piercings_smash when smash
        group multiple auto variant piercings_smash_rest when smash and rest
        group multiple auto variant piercings_smash_bounce when smash and bounce
        group multiple auto variant piercings_smash_pulled when smash and pulled
        group multiple auto variant piercings_smash_notpulled when smash and notpulled

        group glasses auto variant "notsmash_notpulled_haircut" if_all ["notsmash", "notpulled", "haircut"]
        group glasses auto variant "notsmash_pulled_haircut" if_all ["notsmash", "pulled", "haircut"]
        group glasses auto variant "smash_pulled_haircut" if_all ["smash", "pulled", "haircut"]
        group glasses auto variant "smash_notpulled_haircut" if_all ["smash", "notpulled", "haircut"]


        group mike_front auto if_any "mike"

    layeredimage reona double hj jack:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker, PubesPicker, OutfitPicker], npc=reona)

        attribute jacknpc null
        attribute mikenpc null


        group bg auto:
            attribute livingroom default

        always "reona_double_hj_jack_mike_body" if_any ["mikenpc"]
        always "reona_double_hj_jack_jack_body" if_any ["jacknpc"]


        always "reona_double_hj_jack_mike_casual" if_not ["naked"] if_any ["casual"] if_all ["mikenpc"]
        always "reona_double_hj_jack_jack_casual" if_not ["naked"] if_any ["casual"] if_all ["jacknpc"]


        attribute collar null
        group collar auto if_any "collar"


        group dick_mike auto if_any "mikenpc"
        always "reona_double_hj_jack_dick_jack" if_any "jacknpc"


        attribute mikecum null
        group dick_cum_mike auto if_any ["mikecum"]
        attribute jackcum null
        always "reona_double_hj_jack_cum_jack" if_any ["jackcum"]


        attribute speed_mike if_any "mikenpc"
        attribute speed_jack if_any "jacknpc"


        always "reona_double_hj_jack_body"


        group head auto:
            attribute up null default
            attribute down null

        group head auto variant "up" if_any "up"
        group head auto variant "down" if_any "down"


        group mouth auto variant "up" if_any ["up"]:
            attribute opened default
        group mouth auto variant "down" if_any ["down"]:
            attribute mouth_open default
        group mouth_mike auto if_any ["mikenpc"]:
            attribute mike_smile default
        group mouth_jack auto if_any ["jacknpc"]:
            attribute jack_smile default
        attribute tongueout


        always "reona_double_hj_jack_hand_reo"


        group eyes_up auto:
            attribute open null default
            attribute close null

        group eyes_down auto:
            attribute mid null default
            attribute ahegao null
            attribute onmike null
            attribute onjack null

        group eyes auto variant "up_nohaircut" if_all ["up", "nohaircut"]
        group eyes auto variant "up_haircut" if_all ["up", "haircut"]
        group eyes auto variant "down_nohaircut" if_all ["down", "nohaircut"]
        group eyes auto variant "down_haircut" if_all ["down", "haircut"]

        group eyes_mike auto if_any ["mikenpc"]:
            attribute mike_open default
        group eyes_jack auto if_any ["jacknpc"]:
            attribute jack_open default

        group glasses auto variant "up" if_any "up"
        group glasses auto variant "down" if_any "down"


        group multiple auto variant piercings
        group multiple:
            attribute tongue null


        attribute cum_hand_mike if_any ["mikenpc"]
        attribute cum_hand_jack if_any ["jacknpc"]


        attribute pubes


        attribute naked null
        group outfit auto if_not ["naked", "swimsuit", "sexyswimsuit"]
        group top auto
        group bot auto


        attribute hand_boy_mike


        attribute toy_anal
        attribute toy_vaginal


        group hand_touch_jack auto if_any "jacknpc":
            attribute normal default
        attribute squirt
        always "reona_double_hj_jack_hand_touch_jack_handle" if_any ["casual"] if_all ["jacknpc"]


        group water auto if_any ["pool", "beach"]:
            attribute opaque default

    layeredimage reona threesome mikefuck:
        attribute_function Pickers([PiercingsPicker, PubesPicker], npc=reona)


        group bg auto:
            attribute bedroom default


        always "reona_threesome_mikefuck_jack_leg" if_any ["jack"]


        group head auto:
            attribute normal null default
            attribute orgasm null
            attribute blow null

        group head auto variant "normal" if_any "normal"
        group head auto variant "orgasm" if_any "orgasm"


        group mouth auto if_any ["normal"]:
            attribute mouth_normal default

        group eyes auto:
            attribute eyes_open null default
            attribute eyes_close null

        group eyes auto variant "nohaircut" if_all ["normal", "nohaircut"]
        group eyes auto variant "haircut" if_all ["normal", "haircut"]

        group glasses auto variant "normal" if_any "normal"


        attribute facecum if_any ["normal"]


        attribute jack
        always "reona_threesome_mikefuck_dickjack" if_any ["jack"]


        attribute jackcum null
        always "reona_threesome_mikefuck_cum_jack_jack_out" if_all ["jack", "jackcum"] if_not ["blow"]


        attribute hand_jack if_any ["jack"]


        group head auto variant "blow" if_any "blow"


        group cum_jack auto if_all ["jack", "jackcum"]


        always "reona_threesome_mikefuck_bodies"
        attribute pubes


        group multiple auto variant piercings
        group multiple:
            attribute tongue null
        group multiple auto variant piercings_novaginal when not vaginal


        attribute bodycum


        attribute analgape if_not ["plug", "anal"]
        always "reona_threesome_mikefuck_analgape" if_any ["plug"] if_not ["anal"]
        attribute plug if_not ["anal"]


        attribute vaginalgape if_not ["vaginaldrip", "vaginal"]
        always "reona_threesome_mikefuck_vaginalgape" if_any ["vaginaldrip"] if_not ["vaginal"]
        attribute vaginaldrip if_not ["vaginal"]


        attribute beads null
        group beads auto if_any ["beads"] if_not ["vaginal"]:
            attribute inside default


        attribute analdrip if_any ["down"]


        group dick auto:
            attribute down default


        attribute mikecondom null
        group condom auto if_any ["mikecondom"]


        attribute mikecum null
        group cum auto if_any ["mikecum"]


        attribute analdrip if_any ["up", "vaginal", "anal"]


        group multiple auto variant piercings_vaginal when vaginal


        attribute fx if_any ["normal", "orgasm"]

    layeredimage reona threesome jackfuck:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PubesPicker], npc=reona)


        group bg auto:
            attribute bedroom default


        always "reona_threesome_jackfuck_arm_dildo" if_any ["dildo"] if_not ["jack"]
        always "reona_threesome_jackfuck_reona"
        attribute pubes
        attribute collar
        always "reona_threesome_jackfuck_arm_leg" if_not ["dildo"]
        always "reona_threesome_jackfuck_arm_leg" if_any ["jack"]


        attribute bodycum_top
        attribute bodycum_bot


        always "reona_threesome_jackfuck_head_turn" if_all ["mike", "blow"]
        group head auto:
            attribute normal null default
            attribute turn null

        group head auto variant "normal" if_any "normal"
        group head auto variant "turn" if_any "turn"


        group mouth auto:
            attribute mouth_lick null default
            attribute mouth_ahegao null

        group mouth auto variant "normal" if_any "normal"
        group mouth auto variant "turn" if_any "turn"


        group eyes_normal auto:
            attribute eyes_open null default
            attribute eyes_ahegao null
            attribute eyes_close null
            attribute eyes_lookback null

        group eyes_normal auto variant "nohaircut" if_all ["normal", "nohaircut"]
        group eyes_normal auto variant "haircut" if_all ["normal", "haircut"]

        group eyes_turn auto:
            attribute eyes_opened null default
            attribute eyes_closed null

        group eyes_turn auto variant "nohaircut" if_all ["turn", "nohaircut"]
        group eyes_turn auto variant "haircut" if_all ["turn", "haircut"]

        group glasses auto variant "normal" if_any "normal"
        group glasses auto variant "turn" if_any "turn"


        group multiple auto variant piercings_normal when normal


        attribute facecum


        attribute dildo if_not ["jack"]


        group multiple auto variant piercings
        group multiple:
            attribute tongue null


        attribute jack
        group dick_jack auto if_any ["jack"]:
            attribute jack_out default
        attribute jackcum null
        group cum_jack auto if_all ["jack", "jackcum"] if_not ["jackcondom"]:
            attribute jack_out default
        attribute jackcondom null
        group condom_jack auto if_all ["jack", "jackcondom"]:
            attribute jack_out default


        always "reona_threesome_jackfuck_forearm_leg" if_not ["dildo"]
        always "reona_threesome_jackfuck_forearm_leg" if_any ["jack"]
        always "reona_threesome_jackfuck_arm_rest"
        always "reona_threesome_jackfuck_arm_out" if_any ["mike"] if_not ["blow", "handjob"]
        always "reona_threesome_jackfuck_arm_out" if_any ["blow", "handjob"] if_not ["mike"]
        always "reona_threesome_jackfuck_arm_out" if_not ["mike", "blow", "handjob"]


        attribute mike
        group mikedick:
            attribute handjob null
            attribute blow null
        always "reona_threesome_jackfuck_dick_mike_mike_out" if_any ["mike"] if_not ["blow"]
        always "reona_threesome_jackfuck_cum_mike_mike_out" if_all ["mike", "mikecum"] if_not ["blow"]
        group handjob auto if_all ["handjob", "mike"]:
            attribute back default
        attribute mikecum null
        always "reona_threesome_jackfuck_dick_mike_mike_blow" if_all ["mike", "blow"]
        always "reona_threesome_jackfuck_cum_mike_mike_blow" if_all ["mike", "blow", "mikecum"]

    layeredimage reona ending:
        attribute_function Pickers([EndingKidPicker], npc=reona)

        always "reona_ending_bg"
        group bodies auto
        attribute pureglasses
        attribute kid

    layeredimage reona lapdance:
        attribute_function Pickers([HaircutPicker, OutfitPicker, PiercingsPicker, MCCGPicker], npc=reona)

        group bg auto:
            attribute stripclub default

        attribute mikemc null
        attribute naked null

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null

        group mcoutfit auto when not naked:
            attribute mc_casual default

        attribute nonpc null
        always "reona_lapdance_reona" when not nonpc

        group haircuts auto when not nonpc

        attribute collar when not nonpc
        group necklace when not nonpc and not collar

        group exp auto when not nonpc:
            attribute normal default

        group multiple auto variant piercings when not nonpc

        attribute reona_naked null
        attribute innersexy null
        group innertop auto variant casual when not innersexy
        group innertop auto variant sexy when innersexy
        group outfits auto when not (nonpc or naked or reona_naked)

        group acc auto when not (nonpc or naked or reona_naked)

        attribute fuck null
        group fuck auto when fuck and not nonpc


init -35 python:
    reona_attrs = {
    'motions': ['idle'],
    'lefthands': ['leftnormal', 'leftpeace', 'leftback'],
    'righthands': ['rightnormal', 'rightpeace', 'rightok', 'rightopen', 'righthold'],
    'piercings': ['clit', 'navel', 'nipples', 'nose'],
    'haircuts': ['nohaircut', 'haircut'],
    'exps': ['normal', 'angry', 'annoyed', 'devious', 'embarrassed', 'flirt', 'guilty', 'happy', 'interested', 'lying', 'mindless', 'pensive', 'sad', 'sadangry', 'sadfrustrated', 'sadshock', 'sadsmile', 'shock', 'shout', 'shy', 'stuned', 'surprised', 'talkative', 'upset', 'whining'],
    'outfits': ['casual', 'purecasual', 'sport', 'date', 'puredate', 'sexydate', 'sluttydate', 'swimsuit', 'sexyswimsuit', 'rpg', 'halloween', 'wedding', 'underwear', 'sexyunderwear'],
    'others': ['pregnant', 'pubes', 'collar', 'blush', 'bottomless', 'topless', 'naked', 'noacc', 'saliva'],
    'accessories': ['glasses', 'pureglasses', 'dildo', 'mask', 'wallet'],
}

    def reona_anim_filter(attrs, anim_dict=reona_attrs):
        
        if not isinstance(attrs, list):
            attrs = list(attrs)
        
        
        add_pickers_attrs = Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker], npc=reona)(set(attrs))
        if "pregnant_navel" in add_pickers_attrs:
            add_pickers_attrs.remove("pregnant_navel")
            add_pickers_attrs.add("navel")
        attrs.extend(add_pickers_attrs)
        
        
        sgl_attrs, mult_attrs = anim_attrs_filter(attrs,
        {k: [None, anim_dict[k]] for k in ['lefthands', 'righthands', 'exps', 'outfits', 'haircuts']},
        {k: [[], anim_dict[k]] for k in ['motions', 'piercings', 'accessories', 'others']},
        prv_def_vals=['outfits']
    )
        
        
        sgl_attrs['outfits'][0] = (Pickers([OutfitPicker], npc=reona)(set(attrs) if not sgl_attrs['outfits'][0] else {sgl_attrs['outfits'][0]}) & set(anim_dict['outfits']) or {"casual"}).pop()
        
        
        attr_pubes = None
        if 'pubes' in mult_attrs['others'][0]:
            attr_pubes = "pubes_" + sgl_attrs['haircuts'][0]
        
        
        if sgl_attrs['outfits'][0] in ['halloween']:
            sgl_attrs['haircuts'][0] = "haircut_halloween"
        
        
        attr_inner_outfit = None
        if sgl_attrs['outfits'][0] in ['casual', 'date', 'sexydate']:
            if reona.purity < 20 and reona.sub >= 50:
                attr_inner_outfit = "inner_sexyunderwear"
            else:
                attr_inner_outfit = "inner_underwear"
        
        
        attr_acc_head = None
        if 'noacc' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['halloween', 'sexydate', 'wedding']:
            attr_acc_head = "acc_head_" + sgl_attrs['outfits'][0]
        
        
        attr_necklace = None
        if 'collar' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['date', 'sexydate', 'sluttydate']:
            attr_necklace = "necklace_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_hand = None
        if 'noacc' not in mult_attrs['others'][0] and sgl_attrs['outfits'][0] in ['casual', 'date', 'sexydate']:
            attr_acc_hand = "acc_hand_" + sgl_attrs['outfits'][0]
        
        
        attr_jacket = None
        if not any(attr in mult_attrs['others'][0] for attr in ('nojacket', 'bottomless', 'naked', 'pregnant')) and sgl_attrs['outfits'][0] in ['casual']:
            attr_jacket = "jacket_" + sgl_attrs['outfits'][0]
        
        
        attr_acc_tattoo = None
        if sgl_attrs['outfits'][0] in ['halloween']:
            attr_acc_tattoo = "acc_tattoo_" + sgl_attrs['outfits'][0]
        
        
        attr_stockings = None
        if sgl_attrs['outfits'][0] in ['sluttydate']:
            attr_stockings = "stockings_" + sgl_attrs['outfits'][0]
        
        
        attr_wings = None
        if sgl_attrs['outfits'][0] in ['halloween']:
            attr_wings = "wings_" + sgl_attrs['outfits'][0]
        
        
        attr_tail = None
        if sgl_attrs['outfits'][0] in ['halloween']:
            attr_tail = "tail_" + sgl_attrs['outfits'][0]
        
        
        if sgl_attrs['outfits'][0] in ['rpg']:
            sgl_attrs['lefthands'][0] = None
            sgl_attrs['righthands'][0] = None
            if 'glasses' in mult_attrs['accessories'][0]:
                mult_attrs['accessories'][0].remove('glasses')
            if 'pureglasses' in mult_attrs['accessories'][0]:
                mult_attrs['accessories'][0].remove('pureglasses')
            if 'mask' in mult_attrs['accessories'][0]:
                mult_attrs['accessories'][0].remove('mask')
        if 'dildo' in mult_attrs['accessories'][0] and (sgl_attrs['righthands'][0] != 'righthold' or sgl_attrs['outfits'][0] == 'rpg'):
            mult_attrs['accessories'][0].remove('dildo')
        if 'wallet' in mult_attrs['accessories'][0] and (sgl_attrs['lefthands'][0] != 'leftback' or sgl_attrs['outfits'][0] == 'rpg'):
            mult_attrs['accessories'][0].remove('wallet')
        
        
        if all(attr in mult_attrs['others'][0] for attr in ('saliva', 'mask')):
            mult_attrs['others'][0].remove('saliva')
        
        
        sgl_attrs = [attr[0] for attr in sgl_attrs.values()]
        mult_attrs = [attrs for attr_type in mult_attrs for attrs in mult_attrs[attr_type][0]]
        return filtered_attrs('appear', mult_attrs, sgl_attrs, attr_pubes, attr_tail, attr_wings, attr_stockings, attr_acc_tattoo, attr_jacket, attr_acc_hand, attr_necklace, attr_acc_head, attr_inner_outfit)


    def reona_close_anim_filter(attrs, anim_dict=reona_attrs):
        return reona_anim_filter(attrs, anim_dict)

label test_reona_exps:
    $ pose = 'leftnormal rightnormal'

    $ renpy.show(f"reona {pose} angry")
    show expression f"reona {pose} angry" as l2 at left
    "angry"

    $ renpy.show(f"reona {pose} annoyed")
    show expression f"reona {pose} annoyed" as l2 at left
    "annoyed"

    $ renpy.show(f"reona {pose} devious")
    show expression f"reona {pose} devious" as l2 at left
    "devious"

    $ renpy.show(f"reona {pose} embarrassed")
    show expression f"reona {pose} embarrassed" as l2 at left
    "embarrassed"

    $ renpy.show(f"reona {pose} flirt")
    show expression f"reona {pose} flirt" as l2 at left
    "flirt"

    $ renpy.show(f"reona {pose} guilty")
    show expression f"reona {pose} guilty" as l2 at left
    "guilty"

    $ renpy.show(f"reona {pose} happy")
    show expression f"reona {pose} happy" as l2 at left
    "happy"

    $ renpy.show(f"reona {pose} interested")
    show expression f"reona {pose} interested" as l2 at left
    "interested"

    $ renpy.show(f"reona {pose} lying")
    show expression f"reona {pose} lying" as l2 at left
    "lying"

    $ renpy.show(f"reona {pose} mindless")
    show expression f"reona {pose} mindless" as l2 at left
    "mindless"

    $ renpy.show(f"reona {pose} normal")
    show expression f"reona {pose} normal" as l2 at left
    "normal"

    $ renpy.show(f"reona {pose} pensive")
    show expression f"reona {pose} pensive" as l2 at left
    "pensive"

    $ renpy.show(f"reona {pose} sad")
    show expression f"reona {pose} sad" as l2 at left
    "sad"

    $ renpy.show(f"reona {pose} sadangry")
    show expression f"reona {pose} sadangry" as l2 at left
    "sadangry"

    $ renpy.show(f"reona {pose} sadfrustrated")
    show expression f"reona {pose} sadfrustrated" as l2 at left
    "sadfrustrated"

    $ renpy.show(f"reona {pose} sadshock")
    show expression f"reona {pose} sadshock" as l2 at left
    "sadshock"

    $ renpy.show(f"reona {pose} sadsmile")
    show expression f"reona {pose} sadsmile" as l2 at left
    "sadsmile"

    $ renpy.show(f"reona {pose} shock")
    show expression f"reona {pose} shock" as l2 at left
    "shock"

    $ renpy.show(f"reona {pose} shout")
    show expression f"reona {pose} shout" as l2 at left
    "shout"

    $ renpy.show(f"reona {pose} shy")
    show expression f"reona {pose} shy" as l2 at left
    "shy"

    $ renpy.show(f"reona {pose} stuned")
    show expression f"reona {pose} stuned" as l2 at left
    "stuned"

    $ renpy.show(f"reona {pose} surprised")
    show expression f"reona {pose} surprised" as l2 at left
    "surprised"

    $ renpy.show(f"reona {pose} talkative")
    show expression f"reona {pose} talkative" as l2 at left
    "talkative"

    $ renpy.show(f"reona {pose} upset")
    show expression f"reona {pose} upset" as l2 at left
    "upset"

    $ renpy.show(f"reona {pose} whining")
    show expression f"reona {pose} whining" as l2 at left
    "whining"

    return

label test_reona_outfits:
    $ reona.flags.purecasual = False
    $ reona.flags.puredate = False
    $ reona.flags.sexyswimsuit = False
    $ reona.flags.sexydate = False
    $ reona.flags.sluttydate = False
    $ renpy.dynamic(count=0, pregnancy='')
    while count < 2:

        $ renpy.show(f"reona casual{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona casual{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona casual{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona casual{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona casual{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "casual"

        $ renpy.show(f"reona date{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona date{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona date{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona date{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona date{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "date"

        $ renpy.show(f"reona halloween{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona halloween{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona halloween{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona halloween{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona halloween{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "halloween"

        $ renpy.show(f"reona purecasual{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona purecasual{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona purecasual{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona purecasual{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona purecasual{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "purecasual"

        $ renpy.show(f"reona puredate{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona puredate{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona puredate{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona puredate{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona puredate{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "puredate"

        $ renpy.show(f"reona rpg{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona rpg{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona rpg{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona rpg{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona rpg{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "rpg"

        $ renpy.show(f"reona sexydate{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona sexydate{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona sexydate{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona sexydate{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona sexydate{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "sexydate"

        $ renpy.show(f"reona sexyswimsuit{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona sexyswimsuit{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona sexyswimsuit{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona sexyswimsuit{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona sexyswimsuit{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "sexyswimsuit"

        $ renpy.show(f"reona sexyunderwear{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona sexyunderwear{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona sexyunderwear{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona sexyunderwear{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona sexyunderwear{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "sexyunderwear"

        $ renpy.show(f"reona sluttydate{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona sluttydate{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona sluttydate{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona sluttydate{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona sluttydate{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "sluttydate"

        $ renpy.show(f"reona sport{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona sport{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona sport{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona sport{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona sport{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "sport"

        $ renpy.show(f"reona swimsuit{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona swimsuit{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona swimsuit{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona swimsuit{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona swimsuit{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "swimsuit"

        $ renpy.show(f"reona underwear{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona underwear{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona underwear{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona underwear{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona underwear{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "underwear"

        $ renpy.show(f"reona wedding{pregnancy} leftback rightnormal", tag="r1", at_list=[mostleft5])
        $ renpy.show(f"reona wedding{pregnancy} leftnormal rightok", tag="r2", at_list=[left5])
        $ renpy.show(f"reona wedding{pregnancy} leftpeace rightpeace", tag="r3", at_list=[center])
        $ renpy.show(f"reona wedding{pregnancy} leftnormal rightopen", tag="r4", at_list=[right5])
        $ renpy.show(f"reona wedding{pregnancy} leftback righthold", tag="r5", at_list=[mostright5])
        "wedding"

        $ pregnancy = ' pregnant'
        $ count += 1

    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
