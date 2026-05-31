init 1:
    layeredimage sasha:
        attribute_function Pickers([PositionPicker, OutfitPicker, CollarPicker, PregnancyPicker, HaircutPicker, PubesPicker, PiercingsPicker],npc=sasha)


        attribute idle null


        attribute noacc null
        group acc_back auto when not (noacc or naked or bottomless)


        attribute pregnant null
        group position auto when not pregnant
        group position auto variant pregnant when pregnant

        attribute blush


        group exp auto:
            attribute normal default


        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut and not halloween
        group haircut auto variant bb when haircut and boobjob and not halloween


        group wig auto when halloween
        group wig auto variant bb when halloween and boobjob


        attribute boobjob null
        attribute noboobjob null
        group bb auto when boobjob


        attribute pubes when not pregnant
        group pubes auto when pubes


        group acc_tattoo auto


        group multiple auto variant piercings_body
        group multiple auto variant piercings_body_a when a and not boobjob
        group multiple auto variant piercings_body_a_bb when a and boobjob
        group multiple auto variant piercings_body_b when b and not boobjob
        group multiple auto variant piercings_body_b_bb when b and boobjob


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings_face when not sluttydate
        group multiple auto variant piercings_face_sluttydate when sluttydate


        group fx auto


        attribute naked null

        group stockings auto when not (bottomless or naked)

        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked or strapon)
        group bot auto variant a_pregnant when a and pregnant and not (bottomless or naked or strapon)
        group bot auto variant b when b and not (pregnant or bottomless or naked or strapon)
        group bot auto variant b_pregnant when b and pregnant and not (bottomless or naked or strapon)

        attribute topless null
        group top auto variant a when a and not (boobjob or pregnant or topless or naked)
        group top auto variant a_bb when a and boobjob and not (pregnant or topless or naked)
        group top auto variant a_pregnant when a and pregnant and not (boobjob or topless or naked)
        group top auto variant a_pregnant_bb when a and boobjob and pregnant and not (topless or naked)
        group top auto variant b when b and not (boobjob or pregnant or topless or naked)
        group top auto variant b_bb when b and boobjob and not (pregnant or topless or naked)
        group top auto variant b_pregnant when b and pregnant and not (boobjob or topless or naked)
        group top auto variant b_pregnant_bb when b and boobjob and pregnant and not (topless or naked)


        group bot auto variant a when a and strapon and not pregnant
        group bot auto variant a_pregnant when a and pregnant and strapon and not bottomless
        group bot auto variant b when b and strapon and not pregnant
        group bot auto variant b_pregnant when b and pregnant and strapon and not bottomless


        group acc_bot auto variant a when a and not (pregnant or bottomless or naked or noacc)
        group acc_bot auto variant a_pregnant when a and pregnant and not (bottomless or naked or noacc)
        group acc_bot auto variant b when b and not (pregnant or bottomless or naked or noacc)
        group acc_bot auto variant b_pregnant when b and pregnant and not (bottomless or naked or noacc)


        group acc_top auto variant a when a and not (boobjob or topless or naked or noacc)
        group acc_top auto variant a_bb when a and boobjob and not (topless or naked or noacc)
        group acc_top auto variant b when b and not (boobjob or topless or naked or noacc)
        group acc_top auto variant b_bb when b and boobjob and not (topless or naked or noacc)


        group acc_arm auto variant a when a and not (pregnant or naked or noacc or topless)
        group acc_arm auto variant a_pregnant when a and pregnant and not (naked or noacc or topless)
        group acc_arm auto variant b when b and not (pregnant or naked or noacc or topless)
        group acc_arm auto variant b_pregnant when b and pregnant and not (naked or noacc or topless)


        group acc_hand auto variant a when a and not (boobjob or pregnant or naked or noacc or topless)
        group acc_hand auto variant a_bb when a and boobjob and not (pregnant or naked or noacc or topless)
        group acc_hand auto variant a_pregnant when a and pregnant and not (boobjob or naked or noacc or topless)
        group acc_hand auto variant b when b and not (boobjob or pregnant or naked or noacc or topless)
        group acc_hand auto variant b_bb when b and boobjob and not (pregnant or naked or noacc or topless)
        group acc_hand auto variant b_pregnant when b and pregnant and not (boobjob or naked or noacc or topless)


        group acc_head auto when not (naked or noacc or topless)





        attribute collar


        group necklace auto when not collar


        attribute leash when collar
        attribute leash2 when collar


        group arm auto
        group arm auto variant a when a and not bb
        group arm auto variant b when b and not bb
        group arm auto variant a_bb when a and bb
        group arm auto variant b_bb when b and bb


    layeredimage sasha close:
        yalign 0.14
        attribute_function Pickers([PositionPicker, OutfitPicker, CollarPicker, PregnancyPicker, HaircutPicker, PubesPicker, PiercingsPicker],npc=sasha)


        attribute idle null


        attribute noacc null
        group acc_back auto when not (noacc or naked or bottomless)


        attribute pregnant null
        group position auto when not pregnant
        group position auto variant pregnant when pregnant


        attribute blush
        group exp auto:
            attribute normal default


        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut and not halloween
        group haircut auto variant bb when haircut and boobjob and not halloween


        group wig auto when halloween
        group wig auto variant bb when halloween and boobjob


        attribute boobjob null
        attribute noboobjob null
        group bb auto when boobjob


        attribute pubes when not pregnant
        group pubes auto when pubes


        group acc_tattoo auto


        group multiple auto variant piercings_body
        group multiple auto variant piercings_body_a when a and not boobjob
        group multiple auto variant piercings_body_a_bb when a and boobjob
        group multiple auto variant piercings_body_b when b and not boobjob
        group multiple auto variant piercings_body_b_bb when b and boobjob


        attribute lips null
        attribute tongue null
        group multiple auto variant piercings_face when not sluttydate
        group multiple auto variant piercings_face_sluttydate when sluttydate


        group fx auto


        attribute naked null

        group stockings auto when not (bottomless or naked)

        attribute bottomless null
        group bot auto variant a when a and not (pregnant or bottomless or naked)
        group bot auto variant a_pregnant when a and pregnant and not (bottomless or naked)
        group bot auto variant b when b and not (pregnant or bottomless or naked)
        group bot auto variant b_pregnant when b and pregnant and not (bottomless or naked)

        attribute topless null
        group top auto variant a when a and not (boobjob or pregnant or topless or naked)
        group top auto variant a_bb when a and boobjob and not (pregnant or topless or naked)
        group top auto variant a_pregnant when a and pregnant and not (boobjob or topless or naked)
        group top auto variant a_pregnant_bb when a and boobjob and pregnant and not (topless or naked)
        group top auto variant b when b and not (boobjob or pregnant or topless or naked)
        group top auto variant b_bb when b and boobjob and not (pregnant or topless or naked)
        group top auto variant b_pregnant when b and pregnant and not (boobjob or topless or naked)
        group top auto variant b_pregnant_bb when b and boobjob and pregnant and not (topless or naked)


        group acc_bot auto variant a when a and not (pregnant or bottomless or naked or noacc)
        group acc_bot auto variant a_pregnant when a and pregnant and not (bottomless or naked or noacc)
        group acc_bot auto variant b when b and not (pregnant or bottomless or naked or noacc)
        group acc_bot auto variant b_pregnant when b and pregnant and not (bottomless or naked or noacc)


        group acc_top auto variant a when a and not (boobjob or topless or naked or noacc)
        group acc_top auto variant a_bb when a and boobjob and not (topless or naked or noacc)
        group acc_top auto variant b when b and not (boobjob or topless or naked or noacc)
        group acc_top auto variant b_bb when b and boobjob and not (topless or naked or noacc)


        group acc_arm auto variant a when a and not (pregnant or naked or noacc or topless)
        group acc_arm auto variant a_pregnant when a and pregnant and not (naked or noacc or topless)
        group acc_arm auto variant b when b and not (pregnant or naked or noacc or topless)
        group acc_arm auto variant b_pregnant when b and pregnant and not (naked or noacc or topless)


        group acc_hand auto variant a when a and not (boobjob or pregnant or naked or noacc or topless)
        group acc_hand auto variant a_bb when a and boobjob and not (pregnant or naked or noacc or topless)
        group acc_hand auto variant a_pregnant when a and pregnant and not (boobjob or naked or noacc or topless)
        group acc_hand auto variant b when b and not (boobjob or pregnant or naked or noacc or topless)
        group acc_hand auto variant b_bb when b and boobjob and not (pregnant or naked or noacc or topless)
        group acc_hand auto variant b_pregnant when b and pregnant and not (boobjob or naked or noacc or topless)


        group acc_head auto when not (naked or noacc or topless)





        attribute collar


        group necklace auto when not collar


        attribute leash when collar
        attribute leash2 when collar


        group arm auto
        group arm auto variant a when a and not bb
        group arm auto variant b when b and not bb
        group arm auto variant a_bb when a and bb
        group arm auto variant b_bb when b and bb

    layeredimage sasha smartphone:
        always "sasha_smartphone"

    layeredimage sasha ending:
        attribute_function Pickers([CollarPicker, HaircutPicker, EndingKidPicker], npc=sasha)

        attribute sasha


        attribute nohaircut
        attribute haircut
        attribute boobjob
        attribute collar
        always "sasha_ending_mike"


        attribute kid

    layeredimage sasha strap:
        attribute_function Pickers([HaircutPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=sasha)

        attribute pubes null
        attribute tongue null

        always "sasha_strap_bg"

        always "sasha_strap_dick" when not breesuck

        group cum auto:
            attribute cum
            attribute precum

        always "sasha_strap_body"

        attribute pregnant

        always "sasha_strap_hand" when not breesuck

        attribute boobjob

        attribute haircut

        attribute collar

        group multiple auto variant piercings
        group multiple auto variant piercings_boobjob when boobjob
        group multiple auto variant piercings_noboobjob when not boobjob

        group exp auto:
            attribute normal default

        attribute bree

        group bree auto when bree:
            attribute breesmile default

        group cum auto:
            attribute cumbree

        attribute light

    layeredimage sasha kiss:
        attribute_function Pickers([OutfitPicker, HaircutPicker, PregnancyPicker, CollarPicker, PiercingsPicker, MCCGPicker], npc=sasha)

        group dicks:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group base auto when not bowsette
        always "sasha_kiss_base_bowsette" when bowsette

        group arms auto variant mikemc when mikemc and not naked
        group arms auto variant breemc when breemc and not naked


        group pregnancy auto variant mikemc when mikemc
        group pregnancy auto variant breemc when breemc


        attribute noboobjob null
        group body auto variant mikemc when mikemc
        group body auto variant breemc when breemc


        attribute nohaircut null
        attribute mc_nohaircut null
        group hairs auto variant mikemc when mikemc
        group multiple auto variant hairs_breemc when breemc:
            attribute mc_haircut when not bowsette


        group acc_blindfold auto when not naked
        group multiple auto variant accessories_mikemc when mikemc and not naked
        group multiple auto variant accessories_breemc when breemc and not naked


        group wigs auto variant mikemc when mikemc
        group wigs auto variant breemc when breemc


        group multiple auto variant piercings_mikemc when mikemc
        group multiple auto variant piercings_breemc when breemc
        group multiple:
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
            attribute clit null
            attribute mc_ears null
        group multiple auto variant piercings_mikemc_boobjob when boobjob and mikemc
        group multiple auto variant piercings_breemc_boobjob when boobjob and breemc
        group multiple auto variant piercings_mikemc_noboobjob when mikemc and not boobjob
        group multiple auto variant piercings_breemc_noboobjob when breemc and not boobjob

        group mcoutfits auto variant mikemc when mikemc and not (boobjob or naked)
        group mcoutfits auto variant mikemc_boobjob when boobjob and mikemc and not naked


        attribute naked null
        attribute topless null
        group outfits auto variant mikemc when mikemc and not (boobjob or pregnant or naked or topless)
        group outfits auto variant breemc when breemc and not (boobjob or naked or topless)
        group outfits auto variant mikemc_boobjob when boobjob and mikemc and not (pregnant or naked or topless)
        group outfits auto variant breemc_boobjob when boobjob and breemc and not (naked or topless)
        group outfits auto variant mikemc_pregnant when pregnant and mikemc and not (boobjob or naked or topless)
        group outfits auto variant breemc_pregnant when pregnant and breemc and not (boobjob or naked or topless)
        group outfits auto variant mikemc_boobjob_pregnant when boobjob and pregnant and mikemc and not (naked or topless)
        group outfits auto variant breemc_boobjob_pregnant when boobjob and pregnant and breemc and not (naked or topless)


        group skirt auto variant mikemc when mikemc and not naked

        attribute mc_pregnant null
        group mcoutfits auto variant breemc when breemc and not naked
        group mcoutfits auto variant breemc_mc_pregnant when mc_pregnant and breemc and not naked

        group multiple auto variant collars_mikemc when mikemc and not rpg
        group multiple auto variant collars_breemc when breemc and not rpg

        attribute cum

        if sasha.flags.engagedmike:
            "sasha_kiss_accessories_mikemc_ring"

    layeredimage sasha bj:
        attribute_function Pickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker], npc=sasha)

        always "sasha_bj_bg"

        always "sasha_bj_sasha"

        group beads auto:
            attribute nobeads null default


        attribute pregnant
        attribute haircut
        attribute nohaircut null
        attribute boobjob

        group exp auto variant dickout when (dickout or nodick):
            attribute open default
        group exp auto variant dickin when dickin:
            attribute open default

        group outfit auto when not (boobjob or pregnant):
            attribute naked null default

        group outfit auto variant boobjob when boobjob and not pregnant:
            attribute naked null default

        group outfit auto variant pregnant when pregnant and not boobjob:
            attribute naked null default

        group outfit auto variant boobjob_pregnant when boobjob and pregnant:
            attribute naked null default

        attribute collar when collar

        group multiple auto variant piercings
        group multiple:
            attribute navel null
            attribute pregnant_navel null
        group piercings auto variant boobjob when boobjob
        group piercings auto variant noboobjob when not boobjob

        group dick auto when mike:
            attribute dickout default
            attribute nodick null
            attribute dickin when not cumafter

        attribute condom null
        group condom auto when mike and condom

        attribute cum null
        group cum auto when cum and not (cumafter or condom)

        always "sasha_bj_cum_dickout_condom" when cum and condom and dickout


        attribute cumafter null
        group cumafter auto when cumafter and not condom

        always "sasha_bj_cum_dickout_condom" when cumafter and condom and dickout

        attribute handmove null
        group handmove auto when handmove

        attribute mike

    layeredimage sasha stand:
        attribute_function Pickers([PregnancyPicker, PubesPicker, CollarPicker, HaircutPicker, PiercingsPicker, DickPicker, MCCGPicker], npc=sasha)

        attribute insert null

        attribute nobg null

        attribute mc_casual null

        group sashaexp auto:
            attribute normal null default
            attribute pleasure null
            attribute ahegao null


        group bg auto when not nobg:
            attribute bedroom1 default




        always "sasha_stand_mirror_bodies" when (bedroom1 or bedroom2) and not nobg

        group multiple auto variant mirror when (bedroom1 or bedroom2) and not nobg

        group mirror_exp auto when (bedroom1 or bedroom2) and not nobg
        group mirror_acc_mouth auto when (bedroom1 or bedroom2) and not nobg

        group mirror_haircuts auto when (bedroom1 or bedroom2) and not nobg
        group mirror_wig auto when (bedroom1 or bedroom2) and not nobg

        group mirror_acc_head auto when (bedroom1 or bedroom2) and not nobg
        group mirror_acc_head auto when (bedroom1 or bedroom2) and not nobg

        group multiple auto variant mirror_piercings when (bedroom1 or bedroom2) and not nobg
        group multiple auto variant mirror_piercings_noboobjob when (bedroom1 or bedroom2) and not (boobjob or nobg)
        group multiple auto variant mirror_piercings_boobjob when boobjob and (bedroom1 or bedroom2) and not nobg

        group mirror_outfit auto variant noboobjob when not (boobjob or pregnant or nobg) and (bedroom1 or bedroom2)
        group mirror_outfit auto variant noboobjob_pregnant when not (boobjob or nobg) and pregnant and (bedroom1 or bedroom2)
        group mirror_outfit auto variant boobjob when boobjob and not (pregnant or nobg) and (bedroom1 or bedroom2)
        group mirror_outfit auto variant boobjob_pregnant when boobjob and pregnant and (bedroom1 or bedroom2)

        group mirror_bot auto when not (pregnant or nobg) and (bedroom1 or bedroom2)
        group mirror_bot auto variant pregnant when pregnant and (bedroom1 or bedroom2) and not nobg
        group multiple auto variant mirror_top_noboobjob when (bedroom1 or bedroom2) and not (boobjob or nobg)
        group mirror_top auto variant boobjob when boobjob and (bedroom1 or bedroom2) and not nobg

        group mirror_stocking auto when (bedroom1 or bedroom2) and not nobg

        group mirror_collars auto when (bedroom1 or bedroom2) and not nobg

        attribute cumshot null
        always "sasha_stand_mirror_cumshot" when (bedroom1 or bedroom2) and cumshot and not nobg

        group mirror_fg auto when (bedroom1 or bedroom2) and not nobg


        always "sasha_stand_main_sasha"

        group multiple auto variant main

        group main_haircuts auto
        group main_wig auto

        group main_acc_head auto
        group main_acc_head auto

        group multiple auto variant main_piercings
        group main_piercings auto variant noboobjob when not boobjob
        group main_piercings auto variant boobjob when boobjob

        group main_outfit auto variant noboobjob when not (boobjob or pregnant)
        group main_outfit auto variant noboobjob_pregnant when not boobjob and pregnant
        group main_outfit auto variant boobjob when boobjob and not pregnant
        group main_outfit auto variant boobjob_pregnant when boobjob and pregnant

        group main_top auto variant noboobjob when not boobjob
        group main_top auto variant boobjob when boobjob

        group main_bot auto when not pregnant
        group main_bot auto variant pregnant when pregnant

        group main_stocking auto

        group main_collars auto

        group main_dick auto

        attribute beads null
        group main_beads auto when beads
        attribute condom null
        group main_condom auto when condom

        group main_dick_out auto when not (vaginal or anal)

        group main_condom_out auto when not (vaginal or anal) and condom

        attribute cum null
        group main_condomcum auto when condom and cum and not (vaginal or anal)

        group main_cumshot auto when cumshot

        attribute creampie null
        group main_creampie auto when creampie

        group main_cum auto when cum





        group multiple auto variant main_fx


        always "sasha_stand_insert_bg" when insert and (pub or stage or nobg)

        always "sasha_stand_insert_sasha" when insert and (pub or stage or nobg)

        group multiple auto variant insert_collars when insert and (pub or stage or nobg)
        group multiple auto variant insert_haircuts when insert and (pub or stage or nobg)
        group multiple auto variant insert_piercings when insert and (pub or stage or nobg)

        group multiple auto variant insert_exp when insert and (pub or stage or nobg)


        group fx auto

    layeredimage sasha missionary:
        attribute_function MultiPickers([PregnancyPicker, PubesPicker, CollarPicker, HaircutPicker, PiercingsPicker, OutfitPicker, MCCGPicker], npcs=[sasha], append_npc_from_attributes=True)
        attribute nomc null

        group multiple:
            attribute mc_naked null
            attribute sasha_naked null
            attribute sasha_tongue null


        always "sasha_missionary_bg"

        attribute sasha
        attribute sasha_collar
        attribute sasha_pregnant
        attribute sasha_haircut
        attribute sasha_nohaircut null

        attribute leash when collar


        group dicks auto:
            attribute out default
            attribute anal null
            attribute vaginal null

        group dick auto when not nomc

        attribute condom null
        group condom auto when condom


        attribute sasha_pubes



        group bot auto variant fuck when (anal or vaginal) and not sasha_pregnant
        group bot auto variant fuck_pregnant when (anal or vaginal) and sasha_pregnant
        group bot auto variant normal when not (anal or vaginal or sasha_pregnant)
        group bot auto variant normal_pregnant when not (anal or vaginal) and sasha_pregnant


        group outfit auto:
            attribute naked null default
            attribute rope when not pregnant

        attribute sasha_noboobjob
        attribute sasha_boobjob

        group top auto variant boobjob when sasha_boobjob
        group top auto variant noboobjob when not sasha_boobjob


        group exp auto:
            attribute sashanormal default


        group multiple auto variant piercings
        group piercings auto variant boobjob when sasha_boobjob
        group piercings auto variant noboobjob when not sasha_boobjob
        group piercings auto variant rope when not sasha_boobjob and rope


        group dick_out auto when out and not nomc
        group condom_out auto when condom and out and not nomc

        attribute mikemc when not nomc

        attribute bree


        attribute bree_pregnant when bree


        attribute bree_collar null
        attribute bree_leash when bree and leash and bree_collar


        group breeexp when bree:
            attribute breenormal default
        attribute bree_blush when bree

        attribute beads null
        group bree_beads auto when beads


        group fx auto


        attribute creampie null
        group creampie auto when creampie

        attribute cum null
        group cumshot auto when cum and out and not nomc
        group condomcum auto when cum and condom and out and nomc


        attribute speed

    layeredimage sasha doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker, DickPicker], npc=sasha)

        group bg auto:
            attribute bedroom1 default

        always "sasha_doggy_sasha"

        group multiple auto variant sasha
        group multiple:
            attribute nohaircut null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        attribute boobjob

        attribute mouthbeads null
        group exp auto if_not 'mouthbeads':
            attribute waiting default

        group exp auto variant beads if_any 'mouthbeads':
            attribute waiting default

        group outfit auto when not boobjob:
            attribute naked null default
        group outfit auto variant bb when boobjob:
            attribute naked null default


        group multiple auto variant piercings
        group multiple auto variant piercings_boobjob when boobjob
        group multiple auto variant piercings_noboobjob when not boobjob

        group beads auto when not vaginal:
            attribute nobeads null default

        group dick auto when mike and (anal or vaginal)

        group dick auto variant out when mike and not (anal or vaginal)

        always "sasha_doggy_mikepubes" when mike

        attribute cum null
        group cum auto when cum and not (condom or cumafter)

        attribute condom null
        group condom auto when mike and condom and (anal or vaginal) and not (cumafter or cumshot or cum)
        group condom auto variant out when mike and condom and not (anal or vaginal or cumafter or cumshot or cum)

        attribute cumshot null
        group cumshot auto when cumshot and not (condom or anal or vaginal)
        group condomcum auto when condom and (cumshot or cum) and not (anal or vaginal)

        group beads auto when vaginal:
            attribute nobeads null default

        attribute mike

        attribute cumafter null
        group cumafter auto when cumafter and not condom:
            attribute vaginal null

        attribute hand null
        group hand auto:
            attribute nohand null default

    layeredimage sasha tittyfuck:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, DickPicker], npc=sasha)


        group bg auto:
            attribute bedroom1 default


        always "sasha_tittyfuck_bodies"


        group head auto:
            attribute normal default


        attribute haircut null
        group haircut auto when haircut


        attribute collar null
        group collar auto when collar


        group mouth when normal:
            attribute mouthopen
            attribute mouthclosed null default
        group eyes when normal:
            attribute eyesopen null default
            attribute eyesclosed


        attribute facecum when normal


        group dick auto variant normal when normal
        group dick auto variant blow when blow


        attribute cum null
        group cum auto variant normal when normal and cum
        group cum auto variant blow when blow and cum


        group bbfg auto
        attribute blow


        group multiple auto variant piercings
        group multiple auto variant piercings_mouthopen when normal and mouthopen
        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_blow when blow

    layeredimage sasha showersex:
        attribute_function Pickers([PregnancyPicker, HaircutPicker, PiercingsPicker], npc=sasha)
        always "sasha_showersex_bg"
        always "sasha_showersex_body"

        attribute pregnant
        attribute boobjob

        group haircuts auto

        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute nose null
        group piercings auto variant boobjob when boobjob
        group piercings auto variant noboobjob when not boobjob

        always "sasha_showersex_arm"
        always "sasha_showersex_man"
        always "sasha_showersex_wet"

    layeredimage sasha foreplay:
        attribute_function Pickers([CollarPicker, PregnancyPicker, HaircutPicker, PiercingsPicker, PubesPicker, OutfitPicker], npc=sasha)

        attribute nobg null
        group bg auto when not nobg:
            attribute bedroom default

        always "sasha_foreplay_body"

        attribute collar

        attribute pubes

        group dick auto:
            attribute down default

        group exp auto:
            attribute normal default

        attribute pregnant
        attribute boobjob
        attribute haircut
        attribute nohaircut null

        group multiple auto variant piercings
        group multiple:
            attribute lips null
            attribute tongue null

        group piercings auto variant boobjob when boobjob
        group piercings auto variant noboobjob when not boobjob

        group piercings auto variant lips when lips
        group piercings auto variant tongue when tongue

        attribute boxer "sasha_foreplay_boxer"

        group outfit:
            attribute underwear null
            attribute swimsuit null
            attribute rope null
            attribute naked null

        group outfit auto when not (pregnant or boobjob)
        group outfit auto variant pregnant when pregnant and not boobjob
        group outfit auto variant boobjob when not pregnant and boobjob
        group outfit auto variant boobjob_pregnant when pregnant and boobjob

        group multiple auto variant acc

        attribute collar

        group multiple auto variant fx

        group fg auto when not nobg

    layeredimage sasha mast:
        attribute_function Pickers([PregnancyPicker, HaircutPicker, PiercingsPicker], npc=sasha)
        always "sasha_mast_bg"
        always "sasha_mast_body"

        group haircuts auto

        always "sasha_mast_line"
        always "sasha_mast_toys"

        attribute pregnant
        attribute boobjob

        group multiple auto variant piercings
        group piercings auto variant boobjob when boobjob
        group piercings auto variant noboobjob when not boobjob

        always "sasha_mast_pussy" when not pregnant
        always "sasha_mast_pussy_preg" when pregnant

        group left auto:
            attribute normal default

    layeredimage sasha rimjob:
        attribute_function Pickers([PiercingsPicker, HaircutPicker, DickPicker], npc=sasha)


        always "sasha_rimjob_bg"


        always "sasha_rimjob_bodies"


        attribute haircut


        group multiple auto variant piercings


        group dick auto


        attribute cum null
        group cum auto when cum

    layeredimage sasha handjob:
        attribute_function Pickers([PiercingsPicker, HaircutPicker, DickPicker, PregnancyPicker], npc=sasha)


        always "sasha_handjob_bg"
        always "sasha_handjob_bodies"


        attribute pregnant


        attribute boobjob


        group multiple auto variant piercings
        group multiple auto variant piercings_bb when bb


        attribute haircut
        attribute nohaircut


        group dick auto


        attribute cum null
        group cum auto when cum


        always "sasha_handjob_sashahand"


        attribute speed

    layeredimage sasha foot:
        attribute_function Pickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker, OutfitPicker], npc=sasha)

        always "sasha_foot_bg"

        always "sasha_foot_mike"

        group sasha auto

        group boobjob auto when boobjob

        group pregnant auto when pregnant

        attribute nohaircut

        attribute collar

        group multiple auto variant piercings
        group multiple auto variant piercings_notsleep when not sleep
        group multiple auto variant piercings_naked when naked
        group multiple auto variant piercings_naked_bb when naked and boobjob
        group multiple auto variant piercings_naked_notbb when naked and not boobjob

        group feet auto:
            attribute massage default

        attribute cum when footjob

        group mikeexp auto:
            attribute blush default

    layeredimage sasha bj2:
        attribute_function Pickers([CollarPicker, HaircutPicker, OutfitPicker], npc=sasha)

        attribute boobjob null
        attribute noboobjob null

        group bg auto:
            attribute bedroom1 default

        always "sasha_bj2_body"

        attribute naked null
        group outfit auto when not naked

        attribute collar

        group haircuts auto

        group eyes auto:
            attribute opened default
        group mouth auto when not (suck or lick):
            attribute smile default
        group man auto:
            attribute mike default
        group posi auto when not scottie:
            attribute dick default
        group posi auto variant scottie when scottie:
            attribute dick default
        attribute cum null
        group cum auto when cum

    layeredimage sasha bass attack:
        attribute_function Pickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker, OutfitPicker], npc=sasha)

        always "sasha_bass_attack_sasha"
        attribute nohaircut
        attribute pregnant
        attribute boobjob
        group multiple auto variant piercings
        attribute naked null
        group outfit auto when not naked:
            attribute sleep default
        group outfit auto variant pregnant when pregnant and not naked
        group outfit auto variant boobjob when boobjob and not naked
        attribute collar

    layeredimage sasha cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=sasha)

        attribute cum null

        group bg auto:
            attribute bedroom default

        always "sasha_cowgirl_body"

        group haircuts auto

        group exp auto:
            attribute normal default

        attribute collar

        attribute boobjob

        group fuck auto:
            attribute vaginal default

        attribute condom when vaginal:
            "sasha_cowgirl_condom"

        group cum auto when cum and not condom

        attribute pregnant

        group multiple auto variant piercings
        group piercings auto variant boobjob when boobjob
        group piercings auto variant noboobjob when not boobjob

        group outfit auto when not boobjob:
            attribute naked null default
        group outfit auto variant bb when boobjob:
            attribute naked null default

        attribute hands when not boobjob "sasha_cowgirl_hands"
        attribute hands when boobjob "sasha_cowgirl_hands_bb"

    layeredimage sasha restroom sex:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, OutfitPicker], npc=sasha)
        always "sasha_restroom_sex_bg"

        always "sasha_restroom_sex_sasha"

        always "sasha_restroom_sex_mike"

        attribute nohaircut
        attribute collar
        attribute pregnant

        group multiple auto variant outfit
        group multiple auto variant outfit_pregnant when pregnant
        attribute boobjob
        group multiple auto variant outfit_bb when boobjob

        group multiple auto variant piercings
        group multiple auto variant piercings_bb when boobjob and not (casual or sexydate)
        group multiple auto variant piercings_nobb when not (boobjob or casual or sexydate)

        group fx auto

    layeredimage sasha cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker, PubesPicker, MCGenderPicker], npc=sasha)
        attribute shake null
        attribute vibrate null
        attribute nomc null
        attribute notongue null
        attribute nohaircut null
        attribute noboobjob null


        group bg auto:
            attribute bedroom default

        always "sasha_cunnilingus_body_sasha"

        attribute boobjob

        attribute haircut

        group sasha_fx auto

        group exp auto:
            attribute normal default

        attribute pubes

        attribute pregnant

        attribute collar

        group multiple auto variant piercings

        group multiple auto variant piercings_bb when boobjob
        group multiple auto variant piercings_nobb when not boobjob

        group finger_left auto variant mikemc when dildopussy and fingerass and mikemc
        group finger_left auto variant breemc when dildopussy and fingerass and breemc

        group tongue auto variant mikemc when mikemc
        group tongue auto variant breemc when breemc

        group mcbody auto variant still when not (up or middle or down or notongue or nomc)
        group mcbody auto variant lick when (up or middle or down or notongue) and not nomc

        group sasha_hands auto variant bb when boobjob and (up or middle or down)
        group sasha_hands auto variant nobb when not boobjob and (up or middle or down)

        always "sasha_cunnilingus_finger_mikemc_fingerass" when not dildopussy and fingerass and mikemc

        group dildo auto variant mikemc when mikemc
        group dildo auto variant breemc when breemc

        group multiple auto variant fx_shake when shake
        group multiple auto variant fx_vibrate when vibrate

    layeredimage unpack sasha:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=sasha)

        group dicks auto:
            attribute mc_small null
            attribute mc_medium null
            attribute mc_small null

        always "unpack_sasha_bg"

        always "unpack_sasha_body"

        group bodies auto

        attribute mc_nohaircut null
        attribute mc_haircut

        group exp_sasha auto:
            attribute normal default

        group exp auto variant mikemc when mikemc:
            attribute mikenormal default

        group eyes auto variant breemc when breemc:
            attribute down default
        group mouth auto variant breemc when breemc:
            attribute smile default


        group outfit auto
        group outfit auto variant breemc when breemc
        group outfit auto variant mikemc when mikemc:
            attribute mc_casual null

        group hand_position auto:
            attribute search null default
            attribute shown null

        group toys auto:
            attribute vibrator null default
            attribute dildo null

        group hand_mikemc auto when mikemc
        group toy auto variant mikemc when mikemc and shown

        group hand auto variant breemc when breemc
        group hand auto variant breemc_shown when breemc and shown
        group sleeve_breemc auto variant shown when breemc and shown
        group sleeve_breemc auto variant search when breemc and search

        group multiple auto variant fx_breemc when breemc
        group multiple auto variant fx_mikemc when mikemc

    layeredimage bass training:
        attribute_function Pickers([HaircutPicker, PiercingsPicker, OutfitPicker, CollarPicker], npc=sasha)

        always "bass_training_sasha"
        attribute collar
        attribute haircut
        group multiple auto variant piercings
        group outfit auto:
            attribute casual default
        group exp auto:
            attribute opened default
        always "bass_training_hairdetails"

    layeredimage sasha thumb:
        attribute_function Pickers([HaircutPicker, OutfitPicker, PiercingsPicker], npc=sasha)

        attribute nohaircut null

        always "sasha_thumb_bg"

        always "sasha_thumb_body"

        attribute boobjob

        group exp auto:
            attribute normal default

        attribute naked null
        group top auto when not boobjob and not naked

        group top auto variant bb when boobjob and not naked
        group bot auto when not naked

        attribute haircut

        group po auto:
            attribute out default

        group multiple auto variant piercings

        always "sasha_thumb_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
