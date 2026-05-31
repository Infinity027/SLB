init 1:
    layeredimage cassidy:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=cassidy)

        group veil auto variant "a" if_any ["a"]
        group veil auto variant "b" if_any ["b"]


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        attribute blush null
        group blush auto if_any ["blush"]


        attribute facecum null
        group facecum auto if_any ["facecum"]


        attribute wet null
        group wet auto if_any ["wet"]


        attribute pubes null
        group pubes auto if_any ["pubes"]


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute ears null
        attribute nose null

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_sadsmile when a and sadsmile
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_wink when a and wink

        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_sadsmile when b and sadsmile
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_wink when b and wink


        group acc_arm auto variant "a" if_any ["a"] if_not ["naked","topless"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["naked","topless"]


        group acc_neck auto variant "a" if_any ["a"] if_not ["collar"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["collar"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute naked null
        attribute gold null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "b" if_any ["b"] if_not ["naked","bottomless", "pregnant"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","bottomless"]

        group bot auto variant "a_gold" if_all ["a","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "b_gold" if_all ["b","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "a_pregnant_gold" if_all ["a","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant_gold" if_all ["b","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless"]

        group stockings auto variant a when a and not (naked or bottomless)
        group stockings auto variant b when b and not (naked or bottomless)


        group pregnant auto variant "halloween" if_all ["pregnant","halloween"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["naked","topless", "pregnant"]
        group top auto variant "b" if_any ["b"] if_not ["naked","topless", "pregnant"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["naked","topless"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["naked","topless"]

        group top auto variant "a_gold" if_all ["a","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless","pregnant"]
        group top auto variant "b_gold" if_all ["b","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless","pregnant"]
        group top auto variant "a_pregnant_gold" if_all ["a","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless"]
        group top auto variant "b_pregnant_gold" if_all ["b","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless"]


        group chain auto variant "a" if_any ["a"] if_not ["collar"]
        group chain auto variant "b" if_any ["b"] if_not ["collar"]

        group acc auto variant a when a
        group acc auto variant b when b


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage cassidy close:
        yalign 0.16
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=cassidy)

        group veil auto variant "a" if_any ["a"]
        group veil auto variant "b" if_any ["b"]


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        attribute blush null
        group blush auto if_any ["blush"]


        attribute facecum null
        group facecum auto if_any ["facecum"]


        attribute wet null
        group wet auto if_any ["wet"]


        attribute pubes null
        group pubes auto if_any ["pubes"]


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute ears null
        attribute nose null

        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_sadsmile when a and sadsmile
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_wink when a and wink

        group multiple auto variant piercings_b when b
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_sadsmile when b and sadsmile
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_wink when b and wink


        group acc_arm auto variant "a" if_any ["a"] if_not ["naked","topless"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["naked","topless"]


        group acc_neck auto variant "a" if_any ["a"] if_not ["collar"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["collar"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute naked null
        attribute gold null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "b" if_any ["b"] if_not ["naked","bottomless", "pregnant"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["naked","bottomless"]

        group bot auto variant "a_gold" if_all ["a","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "b_gold" if_all ["b","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless","pregnant"]
        group bot auto variant "a_pregnant_gold" if_all ["a","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless"]
        group bot auto variant "b_pregnant_gold" if_all ["b","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","bottomless"]

        group stockings auto variant a when a and not (naked or bottomless)
        group stockings auto variant b when b and not (naked or bottomless)


        group pregnant auto variant "halloween" if_all ["pregnant","halloween"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["naked","topless", "pregnant"]
        group top auto variant "b" if_any ["b"] if_not ["naked","topless", "pregnant"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["naked","topless"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["naked","topless"]

        group top auto variant "a_gold" if_all ["a","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless","pregnant"]
        group top auto variant "b_gold" if_all ["b","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless","pregnant"]
        group top auto variant "a_pregnant_gold" if_all ["a","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless"]
        group top auto variant "b_pregnant_gold" if_all ["b","pregnant","gold"] if_any ["swimsuit","sexyswimsuit"] if_not ["naked","topless"]


        group chain auto variant "a" if_any ["a"] if_not ["collar"]
        group chain auto variant "b" if_any ["b"] if_not ["collar"]

        group acc auto variant a when a
        group acc auto variant b when b


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage cassidy smartphone:
        always "cassidy_smartphone"

    layeredimage cassidy kiss:
        attribute_function Pickers([CollarPicker, OutfitPicker], npc=cassidy)


        always "cassidy_kiss"


        group mikeoutfit auto if_not ["naked"]:
            attribute normal default
            attribute swimsuit null
            attribute sexyswimsuit null


        attribute naked null
        attribute topless null
        group outfit auto if_not ["swimsuit", "sexyswimsuit", "topless", "naked"]
        group outfit auto if_any ["swimsuit", "sexyswimsuit"] if_not ["gold", "topless", "naked"]
        group outfit auto variant "gold" if_all ["gold"] if_any ["swimsuit", "sexyswimsuit"] if_not ["topless", "naked"]


        attribute collar





    layeredimage cassidy tittyfuck:
        attribute_function Pickers([PiercingsPicker, CollarPicker, DickPicker], npc=cassidy)


        group bg auto:
            attribute bedroom default


        always "cassidy_tittyfuck_body" if_not ["blow"]
        always "cassidy_tittyfuck_body_blow" if_any ["blow"]


        attribute collar if_not ["blow"]


        group multiple auto variant piercings


        group eyes auto:
            attribute eyes_open default if_not ["blow"]
        group mouth auto:
            attribute mouth_open default if_not ["blow"]


        attribute cumface
        group tits auto:
            attribute down default

        group multiple auto variant piercings_down when down and not blow
        group multiple auto variant piercings_up when up and not blow
        attribute cumbody


        group base_dick auto
        group dick_down auto if_any ["down"]
        group dick_up auto if_any ["up"]


        attribute cum null
        group cum auto if_any ["cum"]
        group cum auto variant "down" if_all ["cum", "down"]


        attribute blow


        group multiple auto variant piercings_blow when blow

    layeredimage cassidy missionary:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, CollarPicker, PubesPicker, DickPicker], npc=cassidy)

        group multiple:
            attribute ears null
            attribute eyebrow null
            attribute lips null
            attribute tongue null


        always "cassidy_missionary_bg"
        always "cassidy_missionary_mike"
        always "cassidy_missionary_bed"
        always "cassidy_missionary_cassidy"


        attribute collar
        attribute pubes
        attribute pregnant
        group multiple auto variant piercings


        attribute bodycum


        group dick auto:
            attribute out null default
        group multiple auto variant piercings_vaginal when vaginal


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]


        attribute squirt


        group dick auto variant "out" if_any ["out"]


        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]


        group condom auto variant "out" if_all ["condom", "out"]


        group eyes auto:
            attribute eyes_open default
        group mouth auto:
            attribute mouth_normal default


        always "cassidy_missionary_mike_lefthand"
        attribute leash if_any ["collar"]
        always "cassidy_missionary_mike_righthand" if_not ["leash"]

    layeredimage cassidy cunnilingus:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], npc=cassidy)


        group bg auto:
            attribute personal default


        always "cassidy_cunnilingus_bodies"

        group right_arm auto:
            attribute normal default
            attribute hold when naked

        group eyes auto:
            attribute wide default


        attribute pubes


        attribute pregnant


        group multiple auto variant piercings
        group piercings auto variant normal when normal
        group piercings auto variant hold when hold
        group multiple:
            attribute ears null
            attribute tongue null
            attribute lips null


        group top auto when not pregnant:
            attribute naked null
        group top auto variant pregnant when pregnant:
            attribute naked null


        attribute blush




        group mouth auto:
            attribute happy default


        always "cassidy_cunnilingus_mikemc"

        attribute squirt


        always "cassidy_cunnilingus_fg"

    layeredimage cassidy doggy:
        attribute_function Pickers([DickPicker,PregnancyPicker,CollarPicker,PiercingsPicker,XrayPicker], npc=cassidy)


        always "cassidy_doggy_bg"


        always "cassidy_doggy_bodies"


        attribute pregnant


        group multiple auto variant fx


        group exp auto:
            attribute normal default


        group outfit auto


        group dick auto


        attribute xray null
        group xray auto if_any "xray"


        attribute condom null
        group xray_condom auto if_all ["xray","condom"] if_not "creampie"


        group xray_condomcum auto if_all ["xray","condom","creampie"]


        attribute creampie null
        group xray_creampie auto if_all ["xray","creampie"] if_not "condom"


        group dick_out auto if_not ["vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not ["vaginal","anal","condom"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["vaginal","anal","condom"]


        group condom_out auto if_any "condom" if_not ["vaginal","anal","cumshot"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]


        attribute nipples null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings
        group multiple auto variant piercings_ahegao when ahegao
        group multiple auto variant piercings_notahegao when not ahegao


        attribute collar

    layeredimage cassidy cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, DickPicker], npc=cassidy)

        attribute gold null


        group bg auto:
            attribute bedroom default
            attribute beach


        always "cassidy_cowgirl_bodies"


        always "cassidy_cowgirl_light" if_any ["beach"]


        group exp auto:
            attribute normal default
            attribute pleasure
            attribute ahegao


        attribute ears null
        attribute eyebrow null
        attribute lips null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings


        attribute collar


        group dick auto:
            attribute anal
            attribute vaginal


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group multiple auto variant piercings_vaginal when vaginal


        attribute pubes


        attribute pregnant


        group dick auto variant "out" if_not ["vaginal", "anal"]


        group condom auto variant "out" if_any ["condom"] if_not ["cumshot", "vaginal", "anal"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["vaginal", "anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal", "anal"]

    layeredimage cassidy reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, DickPicker], npc=cassidy)


        group bg auto:
            attribute bedroom default


        always "cassidy_reverse_cowgirl_cassidy"


        attribute pubes "cassidy_reverse_cowgirl_pubes" if_not ["vaginal"]


        attribute pregnant


        group exp auto:
            attribute normal default


        attribute collar


        attribute ears null
        attribute gold null
        attribute eyebrow null


        attribute analdrip
        attribute vaginaldrip


        group dick auto
        attribute pubes "cassidy_reverse_cowgirl_pubes_vaginal" if_any ["vaginal"]
        group multiple auto variant piercings

        group outside_dick auto if_not ["anal", "vaginal", "flacid"]


        attribute condom null
        group condom auto if_any ["condom"]
        group outside_condom auto if_not ["anal", "vaginal", "flacid", "cumshot"] if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom"]
        group outside_dickcum auto if_any ["dickcum"] if_not ["anal", "vaginal", "flacid", "condom"]


        group condomcum auto if_all ["condom", "cumshot"]

    layeredimage cassidy ending:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, EndingKidPicker], npc=cassidy)

        always "cassidy_ending_bg"

        attribute pregnant null

        attribute kid

        always "cassidy_ending_cassidy"

        attribute collar

        group multiple auto variant piercings

        always "cassidy_ending_cassidy_casual"
        always "cassidy_ending_fx_cassidy"

        always "cassidy_ending_mike"
        always "cassidy_ending_mike_casual"
        always "cassidy_ending_fx_mike"

        always "cassidy_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
