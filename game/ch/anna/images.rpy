init 1:
    layeredimage anna:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=anna)


        attribute leash if_all ["collar","a"]:
            "anna_leash_a"


        group position auto


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute sticks


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        always:
            if_any ["a"]
            "anna_tattoo_a_heart"


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        group makeup auto variant "a" if_any ["a"]
        group makeup auto variant "b" if_any ["b"]


        group wig auto variant "a" if_any ["a"]
        group wig auto variant "b" if_any ["b"]


        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]


        group cum auto if_any ["ahegao"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute leash if_all ["collar","b"]:
            "anna_leash_b"


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage anna close:
        yalign 0.08
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=anna)


        attribute leash if_all ["collar","a"]:
            "anna_close_leash_a"


        group position auto


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute sticks


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        always:
            if_any ["a"]
            "anna_close_tattoo_a_heart"


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null

        group stockings auto variant "a" if_any ["a"] if_not ["bottomless","naked"]
        group stockings auto variant "b" if_any ["b"] if_not ["bottomless","naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]


        group makeup auto variant "a" if_any ["a"]
        group makeup auto variant "b" if_any ["b"]


        group wig auto variant "a" if_any ["a"]
        group wig auto variant "b" if_any ["b"]


        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]


        group cum auto if_any ["ahegao"]


        attribute collar null
        group collar auto if_any ["collar"]


        attribute leash if_all ["collar","b"]:
            "anna_close_leash_b"


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage anna smartphone:
        always "anna_smartphone"

    layeredimage anna cunnilingus:
        attribute_function Pickers([PubesPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=anna)

        attribute onmike null
        attribute mike null


        always "anna_cunnilingus_bg"


        always "anna_cunnilingus_hand_onbed" if_not ["onmike"]


        always "anna_cunnilingus_anna"


        always "anna_cunnilingus_hand_onmike" if_all ["mike","onmike","lick"]


        group exp auto:
            attribute normal default


        group boobs auto:
            attribute inert default
            attribute squeeze if_all ["lick"]


        attribute pubes


        attribute pregnant


        attribute collar


        attribute ears null
        group multiple auto variant piercings
        group multiple auto variant piercings_inert when inert
        group multiple auto variant piercings_squeeze when squeeze
        group multiple auto variant piercings_notahegao when not ahegao


        group mike auto if_any ["mike"]:
            attribute lick default

    layeredimage anna cowgirl:
        attribute_function Pickers([CollarPicker, PiercingsPicker, XrayPicker], npc=anna)


        always "anna_cowgirl_bg"


        group body auto:
            attribute a default


        always "anna_cowgirl_tattoo" if_any ["b"]


        attribute collar null
        group collar auto if_any ["collar"]


        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        group con:
            attribute condom null
            attribute nocondom null default


        group fuckpos:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto variant "out" if_any ["out"]
        group dick auto variant "vaginal" if_any ["vaginal"]
        group dick auto variant "anal" if_any ["anal"]


        attribute beads if_not ["anal"]


        attribute xray null
        group xray auto variant "anal" if_all ["xray","anal"] if_not ["ass","beads"]
        group xray auto variant "vaginal" if_all ["xray","vaginal"] if_not ["ass","beads"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        group arm:
            attribute rest default
            attribute finger if_not ["anal"]

    layeredimage anna kiss:
        attribute_function Pickers([OutfitPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npc=anna)


        always "anna_kiss"


        group outfitmike auto when not naked:
            attribute normal default


        group multiple auto variant piercings
        group multiple:
            attribute tongue null
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null


        attribute pregnant


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "naked", "topless" ]
        group outfit auto variant "preg" if_any ["pregnant"] if_not ["naked", "topless"]


        group wig auto


        group makeup auto


        attribute collar

    layeredimage anna doggy:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker], npc=anna)


        always "anna_doggy_bg"


        attribute mike
        always "anna_doggy_anna"


        attribute breath
        attribute steam


        group multiple auto variant piercings


        group mouth auto:
            attribute mouth_smile default
        group eyes auto:
            attribute eyes_open default


        attribute mark_right1
        attribute mark_right2
        attribute mark_left1


        attribute sheets


        attribute pregnant


        attribute bodycum


        always "anna_doggy_mikerighthand_grab" if_any ["mike"]


        group dick if_any ["mike"]:
            attribute outside null default
            attribute inside
        group dick auto variant "outside" if_all ["outside", "mike"]


        attribute cum null
        group cum auto variant "outside" if_all ["cum", "outside", "mike"]


        group mikelefthand if_any ["mike"]:
            attribute grab
            attribute spank


    layeredimage anna missionary:
        attribute_function Pickers([CollarPicker, PubesPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=anna)


        always "anna_missionary_bodies"


        attribute nightforest


        attribute pubes


        attribute collar


        group outfit auto


        group wig auto


        group exp auto:
            attribute lookdown default


        attribute leash if_any ["collar"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]:
            attribute naked default


        attribute cum null
        group multiple auto variant cum when cum


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group multiple auto variant piercings
        group multiple auto variant piercings_notvaginal when not vaginal
        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings_openmouth when lookup or ahegao


        group dick_out auto if_not ["vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom","vaginal","anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]


        group condom_out auto if_any ["condom"] if_not ["vaginal","anal","cumshot"]


        group condomcum auto if_all ["cumshot","condom"] if_not ["vaginal","anal"]

    layeredimage anna tittyfuck:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=anna)


        always "anna_tittyfuck_bg"


        always "anna_tittyfuck_body"


        always "anna_tittyfuck_mike"
        always "anna_tittyfuck_dick"


        attribute collar


        group exp auto:
            attribute normal default


        group tits auto:
            attribute down default


        group multiple auto variant piercings
        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_down when down
        attribute tongue null
        group tongue auto if_any ["tongue"]


        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute cum null
        group multiple auto variant cum_up when cum and up
        group multiple auto variant cum_down when cum and down


        attribute speed null
        group speed auto if_all ["speed"]


        group phone_screen auto if_any ["phone"]:
            attribute blank default
            attribute movie null

        always "anna_tittyfuck_phone_bg" if_all ["phone", "movie"]


        always "anna_tittyfuck_phone_body" if_all ["phone", "movie"]


        always "anna_tittyfuck_phone_mike" if_all ["phone", "movie"]
        always "anna_tittyfuck_phone_dick" if_all ["phone", "movie"]

        always "anna_tittyfuck_phone_collar" if_all ["phone", "movie", "collar"]
        group phone_exp auto if_all ["phone", "movie"]


        group phone_tits auto if_all ["phone", "movie"]


        group multiple auto variant phone_piercings when phone and movie
        group multiple auto variant phone_piercings_up when phone and movie and up
        group multiple auto variant phone_piercings_down when phone and movie and down


        group phone_cumshot auto if_any "cumshot" if_all ["phone", "movie"]

        group multiple auto variant phone_cum_up when phone and movie and cum and up
        group multiple auto variant phone_cum_down when phone and movie and cum and down


        group phone_speed auto if_all ["phone", "movie", "speed"]

        always "anna_tittyfuck_phone_overlay" if_any ["phone"]
        attribute phone

    layeredimage anna ending:
        attribute_function Pickers([CollarPicker, EndingKidPicker], npc=anna)


        always "ending_anna_bg"


        always "ending_anna_family"


        attribute kid


        attribute collar

    layeredimage anna blowjob:
        attribute_function Pickers([CollarPicker, PubesPicker, PregnancyPicker, PiercingsPicker, DickPicker], npc=anna)

        always "anna_blowjob_bg"

        always "anna_blowjob_mike"

        attribute suck null
        group dick_inside auto if_any ["suck"]
        group dick_outside auto if_not ["suck"]

        attribute cum null
        group dickcum auto if_all ["cum", "suck"]

        always "anna_blowjob_anna"
        attribute pubes

        attribute pregnant
        attribute collar

        group multiple auto variant piercings

        attribute creampie null
        group creampie auto if_any ["creampie"]

        always "anna_blowjob_open_mouth" if_not ["suck"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        always "anna_blowjob_arm"

    layeredimage anna standing:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker], npc=anna)

        group bg auto:
            attribute bedroom default

        always:
            "anna_standing_bodies"

        group mikehand auto:
            attribute back default
            attribute pull null

        attribute collar
        attribute pregnant

        group hair auto

        attribute blush

        attribute annahand

        group eyes auto:
            attribute normal default
        group mouth auto

        group chest auto:
            attribute still default

        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute tongue null
            attribute ears null
        group piercings auto variant "still" if_any "still"
        group piercings auto variant "wiggle" if_any "wiggle"

        group multiple auto variant fx

        group fg auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
