init 1:
    layeredimage electronic 3some bukkake:
        attribute_function Pickers([PiercingsPicker, CollarPicker], npc=amy)


        always "electronic_3some_bukkake_bg_amylivingroom"


        always "electronic_3some_bukkake_amy_body"


        attribute collar
        group multiple auto variant piercings


        group amyeyes auto:
            attribute eyes_open default


        group amymouth auto:
            attribute mouth_open default


        attribute cumtongueout
        attribute cumrightbreath
        attribute cumleftbreath
        attribute cumbody
        attribute cumfaceright
        attribute cumfaceleft


        attribute amyhandpose


        attribute cumrighthand if_all ["amyhandpose"]
        attribute cumlefthand if_all ["amyhandpose"]


        always "electronic_3some_bukkake_shawndick"

        attribute shawndickcum

        group shawnhand auto if_any ["amyhandpose"]:
            attribute shawnhanddown default

        always "electronic_3some_bukkake_shawn_body"


        always "electronic_3some_bukkake_mikedick"

        attribute mikedickcum

        group mikehand auto if_any ["amyhandpose"]:
            attribute mikehanddown default

        always "electronic_3some_bukkake_mike_body"


        group amylefthand auto if_not ["amyhandpose"]:
            attribute lhanddown default
        group amyrighthand auto if_not ["amyhandpose"]:
            attribute rhanddown default

    layeredimage electronic 3some mikeamydoggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker, PubesPicker, DickPicker], npc=amy)


        always "electronic_3some_mikeamydoggy_bg_house"


        always "electronic_3some_mikeamydoggy_amy_body"


        attribute pubes
        attribute pregnant
        attribute collar
        group multiple auto variant piercings


        attribute butplug


        attribute speedfx


        group amyeyes auto:
            attribute eyes_open default


        group amymouth auto if_not ["blowjob"]:
            attribute mouth_kiss default


        always "electronic_3some_mikeamydoggy_mike_body"


        group multiple auto variant spank
        attribute mikehandspank


        attribute cumbody
        attribute cumface


        group mikedick auto:
            attribute mikeout null default
        group mikedick auto variant "mikeout" if_all ["mikeout"]


        attribute condom null

        group condom auto variant "mikeout" if_all ["condom", "mikeout"] if_not ["mikecum", "mikedickcum"]
        group condomcum auto if_all ["condom", "mikeout"] if_any ["mikecum", "mikedickcum"]


        attribute mikedickcum null
        group mikedickcum auto if_any ["mikedickcum"] if_not ["condom"]


        attribute mikecum null
        group mikecum auto if_any ["mikecum"] if_not ["condom"]
        group mikecum auto variant "mikeout" if_all ["mikecum", "mikeout"] if_not ["condom"]


        attribute shawn null

        attribute blowjob if_any ["shawn"]
        always "electronic_3some_mikeamydoggy_shawn_dickout" if_any ["shawn"] if_not ["blowjob"]

        attribute shawndickcum null
        always "electronic_3some_mikeamydoggy_shawndickcum_blowjob" if_all ["shawn" ,"shawndickcum", "blowjob"]
        always "electronic_3some_mikeamydoggy_shawndickcum_dickout" if_all ["shawn", "shawndickcum"] if_not ["blowjob"]
        attribute shawn


        group amyhand auto:
            attribute normal default
            attribute blowjob if_any ["shawn"]

    layeredimage electronic 3some shawnamyspoon:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, DickPicker], npc=amy)


        always "electronic_3some_shawnamyspoon_bg"
        always "electronic_3some_shawnamyspoon_bodies"


        attribute pubes
        attribute pregnant


        always "electronic_3some_shawnamyspoon_hairnormal" if_not ["hairpulled"]


        group mouth auto if_not ["blowjob"]:
            attribute mouth_pleasure default
        group eyes auto:
            attribute eyes_normal default


        group multiple auto variant piercings


        attribute fingering null
        always "electronic_3some_shawnamyspoon_nofingering" if_not ["fingering"]


        group dick auto:
            attribute out default


        attribute condom null
        always "electronic_3some_shawnamyspoon_condom_out" if_all ["condom", "out"] if_not ["shawncum"]
        always "electronic_3some_shawnamyspoon_condom_vaginal" if_all ["condom", "vaginal"]
        always "electronic_3some_shawnamyspoon_condomcum_out" if_all ["condom", "shawncum", "out"]


        attribute shawncum null
        group shawncum auto if_any ["shawncum"] if_not ["condom"]


        attribute hairpulled if_any ["mike"]
        attribute mike


        attribute blowjob if_any ["mike"]
        group mikedick auto if_any ["mike"] if_not ["blowjob"]


        attribute mikecum null
        group mikecum auto if_all ["mike", "mikecum"] if_not ["blowjob"]
        always "electronic_3some_shawnamyspoon_mikecum_blowjob" if_all ["mike", "mikecum", "blowjob"]

    layeredimage electronic 4some fuckamy:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker], npcs=[amy, palla])


        always "electronic_4some_fuckamy_bg"
        always "electronic_4some_fuckamy_base"


        attribute cum


        group poses auto:
            attribute pose2 default


        attribute amy_pregnant if_any ["pose2"]
        attribute palla_pregnant if_any ["pose1"]


        group collars auto variant "pose1" if_any ["pose1"]
        group collars auto variant "pose2" if_any ["pose2"]


        group multiple auto variant piercings
        group multiple auto variant piercings_pose1 when pose1
        group multiple auto variant piercings_pose2 when pose2

    layeredimage electronic 4some fuckpalla:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[amy, palla])


        always "electronic_4some_fuckpalla_bg"


        attribute shawn


        always "electronic_4some_fuckpalla_pallapulledhair" if_all ["normal", "mike"]
        attribute mike


        group palla auto:
            attribute normal default
        group amy auto:
            attribute normal default
        always "electronic_4some_fuckpalla_mikehand_normal" if_all ["normal", "mike"]


        group collars auto variant "normal" if_any ["normal"]
        group collars auto variant "dildo" if_any ["dildo"]


        group pubes auto variant "normal" if_any ["normal"]
        group pubes auto variant "dildo" if_any ["dildo"]


        group pregnancy auto variant "normal" if_any ["normal"]
        group pregnancy auto variant "dildo" if_any ["dildo"]


        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_dildo when dildo


        attribute shawnholdamy if_all ["normal", "shawn"]
        always "electronic_4some_fuckpalla_amyhand_normal" if_any ["normal"] if_not ["shawn"]
        always "electronic_4some_fuckpalla_amyhand_normal" if_all ["normal", "shawn"] if_not ["shawnholdamy"]
        always "electronic_4some_fuckpalla_shawnhand_normal" if_all ["normal", "shawn"] if_not ["shawnholdamy"]
        always "electronic_4some_fuckpalla_pallahand_normal" if_any ["normal"]


        always "electronic_4some_fuckpalla_pallahair" if_any ["normal"] if_not ["mike"]
        always "electronic_4some_fuckpalla_amyhair" if_any ["normal"]


        attribute dildo



        group shawndick auto if_any ["shawn"] if_not ["dildo"]:
            attribute shawnout default
        always "electronic_4some_fuckpalla_shawndick_shawnout" if_all ["shawn", "dildo"]

        group mikedick auto if_any ["mike"] if_not ["dildo"]:
            attribute mikeout default null
        group mikedick auto variant "mikeout" if_all ["mike", "mikeout"] if_not ["dildo"]
        always "electronic_4some_fuckpalla_mikedick_mikeout_big" if_all ["mike", "big", "dildo"]
        always "electronic_4some_fuckpalla_mikedick_mikeout_medium" if_all ["mike", "medium", "dildo"]
        always "electronic_4some_fuckpalla_mikedick_mikeout_small" if_all ["mike", "small", "dildo"]



        attribute shawncum null
        group shawncum auto if_all ["shawn", "shawncum"] if_not ["shawncondom", "dildo"]
        always "electronic_4some_fuckpalla_shawncum_shawnout" if_all ["shawn", "shawncum", "dildo"] if_not ["shawncondom"]

        attribute mikecum null
        group mikecum auto if_all ["mike", "mikecum"] if_not ["mikecondom", "dildo"]
        group mikecum auto variant "mikeout" if_all ["mike", "mikecum", "mikeout"] if_not ["mikecondom", "dildo"]
        always "electronic_4some_fuckpalla_mikecum_mikeout_big" if_all ["mike", "mikecum", "big", "dildo"] if_not ["mikecondom"]
        always "electronic_4some_fuckpalla_mikecum_mikeout_medium" if_all ["mike", "mikecum", "medium", "dildo"] if_not ["mikecondom"]
        always "electronic_4some_fuckpalla_mikecum_mikeout_small" if_all ["mike", "mikecum", "small", "dildo"] if_not ["mikecondom"]



        attribute shawncondom null
        group shawncondom auto if_all ["shawn", "shawncondom"] if_not ["dildo"]
        always "electronic_4some_fuckpalla_shawncum_shawnout" if_all ["shawn", "shawncondom", "dildo"]

        attribute mikecondom null
        group mikecondom auto if_all ["mike", "mikecondom"] if_not ["dildo"]
        group mikecondom auto variant "mikeout" if_all ["mike", "mikecondom", "mikeout"] if_not ["mikecum", "dildo"]
        always "electronic_4some_fuckpalla_mikecondom_mikeout_big" if_all ["mike", "mikecondom", "big", "dildo"] if_not ["mikecum"]
        always "electronic_4some_fuckpalla_mikecondom_mikeout_medium" if_all ["mike", "mikecondom", "medium", "dildo"] if_not ["mikecum"]
        always "electronic_4some_fuckpalla_mikecondom_mikeout_small" if_all ["mike", "mikecondom", "small", "dildo"] if_not ["mikecum"]
        group mikecondomcum auto if_all ["mike", "mikecondom", "mikecum", "mikeout"] if_not ["dildo"]
        always "electronic_4some_fuckpalla_mikecondomcum_big" if_all ["mike", "mikecondom", "mikecum", "big", "dildo"]
        always "electronic_4some_fuckpalla_mikecondomcum_medium" if_all ["mike", "mikecondom", "mikecum", "medium", "dildo"]
        always "electronic_4some_fuckpalla_mikecondomcum_small" if_all ["mike", "mikecondom", "mikecum", "small", "dildo"]

    layeredimage electronic 4some bj:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker], append_npc_from_attributes=True)


        always "electronic_4some_bj_bg"
        always "electronic_4some_bj_pallaback" if_not ["palla"]
        always "electronic_4some_bj_amyback" if_not ["amy"]



        always "electronic_4some_bj_mikeleg_amyhandjob" if_any ["mike"] if_not ["amy", "palla"]
        group mikeleg if_all ["mike", "amy"]:
            attribute amyhandjob default
            attribute amyblowjob
        always "electronic_4some_bj_mikeleg_onpalla" if_all ["mike", "palla"] if_not ["amy"]

        always "electronic_4some_bj_shawnleg_pallahandjob" if_any ["shawn"] if_not ["palla", "amy"]
        group shawnleg if_all ["shawn", "palla"]:
            attribute pallahandjob default
            attribute pallablowjob
        always "electronic_4some_bj_shawnleg_onamy" if_all ["shawn", "amy"] if_not ["palla"]


        attribute palla

        group pallaeyes auto if_any ["palla"]:
            attribute palla_eyes_open default

        always "electronic_4some_bj_pallamouth" if_any ["palla"] if_not ["shawn"]
        always "electronic_4some_bj_pallamouth" if_all ["palla", "shawn"] if_not ["pallablowjob"]

        attribute palla_pubes if_any ["palla"]

        attribute palla_pregnant if_any ["palla"]

        attribute palla_collar if_any ["palla"]

        group multiple auto variant piercings_palla when palla

        always "electronic_4some_bj_pallafingering" if_any ["palla"] if_not ["mike"]
        always "electronic_4some_bj_pallafingering" if_all ["palla", "amy", "mike"]

        attribute pallabodycum if_any ["palla"]
        attribute pallafacecum if_any ["palla"]


        attribute amy

        always "electronic_4some_bj_amyeyes_amy_eyes_open" if_any ["amy"]

        always "electronic_4some_bj_amymouth" if_any ["amy"] if_not ["mike"]
        always "electronic_4some_bj_amymouth" if_all ["amy", "mike"] if_not ["amyblowjob"]

        attribute amy_pubes if_any ["amy"]

        attribute amy_pregnant if_any ["amy"]

        attribute amy_collar if_any ["amy"]

        group multiple auto variant piercings_amy when amy
        group multiple auto variant piercings_amy_noplayleftboob when amy and not playleftboob
        group multiple auto variant piercings_amy_noplayrightboob when amy and not playrightboob


        always "electronic_4some_bj_amyrighthand_playrightboob" if_any ["amy"] if_not ["mike"]
        group amyrighthand if_all ["amy", "mike"]:
            attribute playrightboob
        group multiple auto variant piercings_amy_playrightboob when amy and not mike
        group multiple auto variant piercings_amy_playrightboob when amy and mike and playrightboob

        always "electronic_4some_bj_amyfingering" if_any ["amy"] if_not ["shawn", "playleftboob"]
        always "electronic_4some_bj_amyfingering" if_all ["amy", "palla", "shawn"] if_not ["playleftboob"]
        group amylefthand if_any ["amy"]:
            attribute playleftboob
        group multiple auto variant piercings_amy_playleftboob when amy and playleftboob

        always "electronic_4some_bj_amyhair" if_any ["amy"]

        attribute amybodycum if_any ["amy"]
        attribute amyfacecum if_any ["amy"]



        attribute mike null
        always "electronic_4some_bj_mike_amyhandjob" if_any ["mike"] if_not ["amy", "palla"]
        group mike if_all ["mike", "amy"]:
            attribute amyhandjob default
            attribute amyblowjob
        always "electronic_4some_bj_mike_onpalla" if_all ["mike", "palla"] if_not ["amy"]

        attribute mikecum null
        always "electronic_4some_bj_mikecum_amyhandjob" if_all ["mike", "mikecum"] if_not ["amy", "palla"]
        group mikecum if_all ["mike", "mikecum", "amy"]:
            attribute amyhandjob default
            attribute amyblowjob
        always "electronic_4some_bj_mikecum_onpalla" if_all ["mike", "mikecum", "palla"] if_not ["amy"]



        attribute shawn null
        always "electronic_4some_bj_shawn_pallahandjob" if_any ["shawn"] if_not ["palla", "amy"]
        group shawn if_all ["shawn", "palla"]:
            attribute pallahandjob default
            attribute pallablowjob
        always "electronic_4some_bj_shawn_onamy" if_all ["shawn", "amy"] if_not ["palla"]

        attribute shawncum null
        always "electronic_4some_bj_shawncum_pallahandjob" if_all ["shawn", "shawncum"] if_not ["palla", "amy"]
        group shawncum if_all ["shawn", "shawncum", "palla"]:
            attribute pallahandjob default
            attribute pallablowjob
        always "electronic_4some_bj_shawncum_onamy" if_all ["shawn", "shawncum", "amy"] if_not ["palla"]




        group amyhandjobmike auto if_all ["amy", "mike", "amyhandjob"] if_not ["playrightboob"]:
            attribute amyback default

        group amyhandjobshawn auto if_all ["amy", "shawn"] if_not ["palla", "playleftboob"]:
            attribute amyback default


        group pallahandjobmike auto if_all ["palla", "mike"] if_not ["amy"]:
            attribute pallaback default

        group pallahandjobshawn auto if_all ["palla", "shawn", "pallahandjob"]:
            attribute pallaback default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
