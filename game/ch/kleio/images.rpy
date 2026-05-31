init 1:
    layeredimage kleio:
        attribute_function Pickers([PositionPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=kleio)


        group position:
            attribute a null
            attribute b null
            attribute bbis null
            attribute c null
            attribute d null


        always:
            if_not ["c"]
            "kleio_body"
        always:
            if_any ["c"]
            if_not ["wolf", "angel"]
            "kleio_body_c"
        group tattoo auto variant "c" if_any "c"



        attribute pubes if_not ["c"]


        group preg auto if_not ["c"]
        group pregc auto if_any ["c"]


        group multiple auto variant piercings when not c


        group tattoo auto variant "bot" if_not ["c"]


        attribute naked null
        group stockings auto if_not ["c", "bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]


        attribute bottomless null
        group bot auto if_not ["pregnant", "c", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["c", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant_c" if_all ["pregnant", "c"] if_not ["bottomless", "naked"]


        group chain auto if_not ["c", "bottomless", "naked"]


        attribute topless null
        group top auto if_not ["pregnant", "c", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["c", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant_c" if_all ["pregnant", "c"] if_not ["topless", "naked"]


        attribute nojacket null
        group jacket auto if_not ["c", "nojacket", "topless", "naked"]
        group jacket auto variant "c" if_any ["c"] if_not ["nojacket", "topless", "naked"]


        group handpos:
            attribute a
            attribute b
            attribute bbis


        group top auto variant "arms_a" if_any ["a"] if_not ["topless", "naked"]
        group top auto variant "arms_b" if_any ["b"] if_not ["topless", "naked"]
        group top auto variant "arms_bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group top auto variant "arms_c" if_any ["c"] if_not ["topless", "naked"]


        group jacket auto variant "arms_a" if_any ["a"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_b" if_any ["b"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_bbis" if_any ["bbis"] if_not ["nojacket", "topless", "naked"]


        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]


        group tattoo auto variant "top_a" if_any ["a"]
        group tattoo auto variant "top_b" if_any ["b"]
        group tattoo auto variant "top_bbis" if_any ["bbis"]
        group tattoo auto variant "top_c" if_any ["c"]
        group tattoo auto variant "top_d" if_any ["d"]


        attribute blush null
        group blush auto if_any ["blush"]


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "bbis" if_any ["bbis"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default
        group exp auto variant "d" if_any ["d"]:
            attribute normal default


        group multiple auto variant piercings_face_a when face_a
        group multiple auto variant piercings_face_b when face_b
        group multiple auto variant piercings_face_bbis when face_bbis
        group multiple auto variant piercings_face_c when face_c
        group multiple auto variant piercings_face_d when face_d

        attribute tongue null
        group multiple auto variant piercings_face_a_tongue when a and tongue
        group multiple auto variant piercings_face_b_tongue when b and tongue
        group multiple auto variant piercings_face_bbis_tongue when bbis and tongue
        group multiple auto variant piercings_face_c_tongue when c and tongue
        group multiple auto variant piercings_face_d_tongue when d and tongue


        group googles auto if_not ["noacc", "topless", "naked"]


        group handpos:
            attribute d


        group top auto variant "arms_d" if_any ["d"] if_not ["topless", "naked"]


        group jacket auto variant "arms_d" if_any ["d"] if_not ["nojacket", "topless", "naked"]


        group gloves auto variant "d" if_any ["d"] if_not ["topless", "naked"]


        attribute noacc null
        group acc auto variant "hand_a" if_any ["a"] if_not ["noacc"]
        group acc auto variant "hand_b" if_any ["b"] if_not ["noacc"]
        group acc auto variant "hand_bbis" if_any ["bbis"] if_not ["noacc"]


        attribute mic if_any ["a", "bbis"] if_not ["noacc", "work", "halloween"]


        attribute collar null
        group collar auto if_any ["collar"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "bbis" if_any ["bbis"]
        group arm auto variant "c" if_any ["c"]
        group arm auto variant "d" if_any ["d"]

    layeredimage kleio close:
        yalign 0.25
        attribute_function Pickers([PositionPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=kleio)


        group position:
            attribute a null
            attribute b null
            attribute bbis null
            attribute c null
            attribute d null


        always:
            if_not ["c"]
            "kleio_close_body"
        always:
            if_any ["c"]
            if_not ["wolf", "angel"]
            "kleio_close_body_c"
        group tattoo auto variant "c" if_any "c"


        attribute pubes if_not ["c"]


        group preg auto if_not ["c"]
        group pregc auto if_any ["c"]


        group multiple auto variant piercings when not c


        group tattoo auto variant "bot" if_not ["c"]


        attribute naked null
        group stockings auto if_not ["c", "bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]


        attribute bottomless null
        group bot auto if_not ["pregnant", "c", "bottomless", "naked"]
        group bot auto variant "pregnant" if_any ["pregnant"] if_not ["c", "bottomless", "naked"]
        group bot auto variant "c" if_any ["c"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "pregnant_c" if_all ["pregnant", "c"] if_not ["bottomless", "naked"]


        group chain auto if_not ["c", "bottomless", "naked"]


        attribute topless null
        group top auto if_not ["pregnant", "c", "topless", "naked"]
        group top auto variant "pregnant" if_any ["pregnant"] if_not ["c", "topless", "naked"]
        group top auto variant "c" if_any ["c"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "pregnant_c" if_all ["pregnant", "c"] if_not ["topless", "naked"]


        attribute nojacket null
        group jacket auto if_not ["c", "nojacket", "topless", "naked"]
        group jacket auto variant "c" if_any ["c"] if_not ["nojacket", "topless", "naked"]


        group handpos:
            attribute a
            attribute b
            attribute bbis


        group top auto variant "arms_a" if_any ["a"] if_not ["topless", "naked"]
        group top auto variant "arms_b" if_any ["b"] if_not ["topless", "naked"]
        group top auto variant "arms_bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group top auto variant "arms_c" if_any ["c"] if_not ["topless", "naked"]


        group jacket auto variant "arms_a" if_any ["a"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_b" if_any ["b"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_bbis" if_any ["bbis"] if_not ["nojacket", "topless", "naked"]


        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]


        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]


        group tattoo auto variant "top_a" if_any ["a"]
        group tattoo auto variant "top_b" if_any ["b"]
        group tattoo auto variant "top_bbis" if_any ["bbis"]
        group tattoo auto variant "top_c" if_any ["c"]
        group tattoo auto variant "top_d" if_any ["d"]


        attribute blush null
        group blush auto if_any ["blush"]


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "bbis" if_any ["bbis"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default
        group exp auto variant "d" if_any ["d"]:
            attribute normal default


        group multiple auto variant piercings_face_a when face_a
        group multiple auto variant piercings_face_b when face_b
        group multiple auto variant piercings_face_bbis when face_bbis
        group multiple auto variant piercings_face_c when face_c
        group multiple auto variant piercings_face_d when face_d

        attribute tongue null
        group multiple auto variant piercings_face_a_tongue when a and tongue
        group multiple auto variant piercings_face_b_tongue when b and tongue
        group multiple auto variant piercings_face_bbis_tongue when bbis and tongue
        group multiple auto variant piercings_face_c_tongue when c and tongue
        group multiple auto variant piercings_face_d_tongue when d and tongue


        group googles auto if_not ["noacc", "topless", "naked"]


        group handpos:
            attribute d


        group top auto variant "arms_d" if_any ["d"] if_not ["topless", "naked"]


        group jacket auto variant "arms_d" if_any ["d"] if_not ["nojacket", "topless", "naked"]


        group gloves auto variant "d" if_any ["d"] if_not ["topless", "naked"]


        attribute noacc null
        group acc auto variant "hand_a" if_any ["a"] if_not ["noacc"]
        group acc auto variant "hand_b" if_any ["b"] if_not ["noacc"]
        group acc auto variant "hand_bbis" if_any ["bbis"] if_not ["noacc"]


        attribute mic if_any ["a", "bbis"] if_not ["noacc", "work", "halloween"]


        attribute collar null
        group collar auto if_any ["collar"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "bbis" if_any ["bbis"]
        group arm auto variant "c" if_any ["c"]
        group arm auto variant "d" if_any ["d"]

    layeredimage kleio smartphone:
        always "kleio_smartphone"

    layeredimage kleio rough:
        attribute_function Pickers([PubesPicker, HaircutPicker, CollarPicker, PregnancyPicker, DickPicker, PiercingsPicker], npc=kleio)


        group bg auto:
            attribute studio default


        always "kleio_rough_kleio"


        attribute nohaircut null
        attribute haircut


        attribute pubes


        group exp auto if_not ["stomp"]:
            attribute normal default
        group exp auto variant "stomp" if_any ["stomp"]:
            attribute normal default


        attribute collar


        group multiple auto variant piercings_body


        group tattoo auto
        group acc_legs auto
        group outfit auto


        attribute pregnant


        group multiple auto variant piercings


        group mike auto:
            attribute pile default



        group dick auto

        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]

        attribute condom null
        group condom auto if_any ["condom"]

        group multiple auto variant piercings_vaginal when vaginal



        group dick_outside auto if_not ["vaginal", "anal"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal", "anal"]

        group condom_outside auto if_any ["condom"] if_not ["condomcum", "vaginal", "anal"]

        attribute condomcum null
        group condomcum_outside auto if_any ["condomcum"] if_not ["condom", "vaginal", "anal"]

    layeredimage kleio kiss:
        attribute_function Pickers([OutfitPicker, HaircutPicker, CollarPicker, PiercingsPicker], npc=kleio)


        always "kleio_kiss"


        group multiple:
            attribute angel null
            attribute wolf null


        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        group multiple auto variant piercings


        group outfitmike auto when not naked:
            attribute normal default


        attribute naked null
        attribute topless null

        group outfit auto if_not ["naked", "topless"]


        attribute collar

        group jacket auto if_not ["naked", "topless"]


        attribute nohaircut null
        attribute haircut


        group gloves auto if_not ["naked"]

    layeredimage kleio cunnilingus:
        attribute_function Pickers([PiercingsPicker, HaircutPicker, PregnancyPicker, CollarPicker, PubesPicker], npc=kleio)


        group bodies auto:
            attribute alone default


        attribute beads null
        group beads auto if_any ["beads"]


        attribute assfinger null
        group assfinger auto if_all ["assfinger","alone"]:
            attribute one default


        attribute dildo null
        group dildo auto if_all ["dildo","alone"]:
            attribute solo default
        attribute speed if_all ["alone","dildo","solo"]


        attribute pubes null
        group pubes auto if_any ["pubes"]


        attribute pregnant


        group exp auto:
            attribute normal default


        attribute collar


        attribute clit null
        group multiple auto variant piercings
        group multiple auto variant piercings_ahegao when ahegao
        group multiple auto variant piercings_alone when alone
        group multiple auto variant piercings_lick when lick


        attribute nohaircut null
        attribute haircut

    layeredimage kleio doggy:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, PregnancyPicker, DickPicker, XrayPicker], npc=kleio)


        always "kleio_doggy_bg"


        attribute smoke


        always "kleio_doggy_kleio"


        group multiple auto variant piercings


        attribute pregnant


        group tattoo auto


        group exp auto:
            attribute normal default


        attribute haircut
        attribute nohaircut null


        attribute sweat


        attribute collar


        attribute mike

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto if_all "mike" if_not ["out"]
        group dick auto variant "out" if_all ["mike", "out"]


        attribute creampie null
        group creampie auto if_all ["mike"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto if_all ["mike", "out", "dickcum"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "out", "cumshot"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "out", "condom"] if_not ["cumshot"]
        group condomcum if_all ["mike", "out", "condom", "cumshot"]


        attribute xray null
        group xray_dick auto if_all ["mike", "xray"]


        group xray_creampie auto if_all ["mike", "xray", "creampie"] if_not ["condom"]


        group xray_condom auto if_all ["mike", "xray", "condom"] if_not ["creampie", "out"]
        group xray_condom auto variant "creampie" if_all ["mike", "xray", "condom", "creampie"]


        attribute squirt


        attribute naked null
        always "kleio_doggy_acc_arm" if_not ["naked"]


        attribute shake


        always "kleio_doggy_light"

    layeredimage kleio bj:
        attribute_function Pickers([PiercingsPicker, HaircutPicker, CollarPicker, DickPicker, OutfitPicker], npc=kleio)

        group bg auto:
            attribute studio default

        always "kleio_bj_mike"
        always "kleio_bj_kleio"

        attribute naked null
        group outfits auto if_not ["naked"]

        attribute collar

        group head auto:
            attribute out default

        always "kleio_bj_exp_headup_normal" if_not ["deep"]
        always "kleio_bj_exp_headdown_normal" if_any ["deep"]

        group multiple auto variant piercings_suck when suck
        group multiple auto variant piercings_deep when deep

        group mouth auto

        group multiple auto variant piercings_lick when lick or out

        group hairs auto variant "headup" if_not ["deep"]
        group hairs auto variant "headdown" if_any ["deep"]

        group dick auto if_not ["lick"]
        group dick auto variant "lick" if_any "lick"

        attribute dickcum null
        group dickcum auto if_any ["dickcum"]

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        attribute cum null
        group cum auto if_any ["cum"]

        attribute facial

        group hands auto:
            attribute still default

        always "kleio_bj_fg"

    layeredimage kleio cowgirl:
        attribute_function Pickers([DickPicker, HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, PubesPicker], npc=kleio)


        always "kleio_cowgirl_bg"


        attribute pubes


        attribute pregnant


        attribute cum null
        group multiple auto variant cum when cum


        group exp auto:
            attribute normal default


        attribute collar


        group multiple auto variant piercings
        group multiple auto variant piercings_notnormal when not normal
        group multiple auto variant piercings_vaginal when vaginal


        attribute nohaircut null
        attribute haircut


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group dick_out auto if_not ["vaginal","anal"]


        group condom_out auto if_any ["condom"] if_not ["cumshot","vaginal","anal"]


        group condomcum auto if_all ["condom","cumshot"] if_not ["vaginal","anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom","vaginal","anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]

    layeredimage kleio_doggy2:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, PregnancyPicker, DickPicker, XrayPicker], npc=kleio)


        always "kleio_doggy2_bg"


        always "kleio_doggy2_kleio"


        group multiple auto variant piercings
        group piercings auto variant "normal" if_not ["vaginal"]
        group multiple auto variant piercings_vaginal when vaginal


        attribute pregnant


        group exp auto:
            attribute normal default


        attribute haircut
        attribute nohaircut null


        attribute collar


        attribute mike

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto if_all "mike" if_not ["out"]
        group dick auto variant "out" if_all ["mike", "out"]


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["condom", "out"]


        attribute dickcum null
        group dickcum auto if_all ["mike", "out", "dickcum"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "out", "cumshot"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "out", "condom"] if_not ["cumshot"]
        group condomcum if_all ["mike", "out", "condom", "cumshot"]


        attribute naked null
        always "kleio_doggy2_acc_arm" if_not ["naked"]


        always "kleio_doggy2_light"

    layeredimage kleio missionary:
        attribute_function Pickers([PubesPicker, PregnancyPicker, PiercingsPicker, CollarPicker, HaircutPicker, DickPicker], npc=kleio)

        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        always "kleio_missionary_bg"


        attribute mike


        always "kleio_missionary_kleio"


        attribute naked null
        always "kleio_missionary_acc_arm" if_not ["naked"]


        attribute pubes


        attribute sweat


        attribute blush


        group exp auto:
            attribute flirt default


        attribute haircut
        attribute nohaircut null


        attribute pregnant


        group multiple auto variant piercings
        group multiple auto variant piercings_notflirt when not flirt


        attribute collar


        group dick auto if_any ["mike"]
        group dick auto variant "out" if_all ["mike", "out"]


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "out", "cumshot"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["mike", "out", "condom", "cumshot"]


        always "kleio_missionary_light"


    layeredimage kleio reverse cowgirl:
        attribute_function Pickers([DickPicker, HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker, PubesPicker], npc=kleio)


        group bg auto:
            attribute bedroom1 default


        always:
            "kleio_reverse_cowgirl_bodies"


        group leftarm auto:
            attribute empty default


        always:
            if_any ["pub", "stage"]
            "kleio_reverse_cowgirl_soundsys"


        always:
            "kleio_reverse_cowgirl_balls"


        attribute pubes


        attribute pregnant


        attribute collar


        group head auto:
            attribute front default


        group keyes auto if_any ["front"]:
            attribute open default


        group kmouth auto if_any ["front"]:
            attribute normal default


        group multiple auto variant piercings
        group multiple auto variant piercings_notpregnant when not pregnant
        group multiple auto variant piercings_face when face


        attribute nohaircut if_not ["back"]
        attribute haircut if_not ["back"]


        group rightarm auto:
            attribute fist default


        group boobs auto:
            attribute down default


        group multiple auto variant piercings_up when up
        group multiple auto variant piercings_down when down


        attribute vaginal null
        attribute anal null

        group dick auto:
            attribute flacid null
            attribute hard default null
        group dick auto variant "hard" if_any ["hard"]
        group dick auto variant "flacid" if_any ["flacid"]


        attribute condom null
        group condom auto if_any ["condom"]


        attribute cum null
        group multiple auto variant cum when cum and not condom


        group condom_out auto if_any ["condom"] if_not ["cumshot","vaginal","anal"]


        attribute aftercum
        group aftercum auto if_any ["aftercum"] if_not ["condom","vaginal","anal", "hard"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]


        attribute squirte


        always:
            if_any ["pub", "stage"]
            "kleio_reverse_cowgirl_fg_crowd"


    layeredimage kleio ending:
        attribute_function Pickers([CollarPicker, PiercingsPicker, OutfitPicker, EndingKidPicker], npc=kleio)

        always "kleio_ending_bg"
        always "kleio_ending_mike"

        always "kleio_ending_kleio"

        attribute collar

        group multiple auto variant piercings

        group outfit auto

        attribute kid

        always "kleio_ending_fg"

    layeredimage kleio kart:
        attribute_function Pickers([CollarPicker, PiercingsPicker, HaircutPicker], npc=kleio)

        attribute bg null
        always "kleio_kart_bg" if_any ["bg"]

        attribute kleio null
        always "kleio_kart_kleionpc" if_any ["kleio"]

        attribute mike null
        always "kleio_kart_mikemc" if_any ["mike"]


        attribute collar


        group multiple auto variant piercings when kleio


        group kleiohair auto if_any ["kleio"]


    layeredimage kleio carsex:
        attribute_function Pickers([DickPicker, HaircutPicker, PregnancyPicker, PiercingsPicker, CollarPicker], npc=kleio)


        always "kleio_carsex_bg"


        always "kleio_carsex_bodies"


        attribute hand


        attribute pregnant


        attribute collar


        group keyes auto:
            attribute open default


        group kmouth auto:
            attribute normal default


        attribute clit null
        attribute ears null
        attribute navel null
        attribute tongue null
        group multiple auto variant piercings


        attribute naked null
        group outfit auto if_not ["pregnant", "naked"]:
            attribute casual default
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked"]:
            attribute casual default


        group hair auto:
            attribute nohaircut default


        attribute creampie


        attribute bodycum


        group karm auto:
            attribute fuck default


        group dick auto if_not ["vaginal","anal"]
        always "kleio_carsex_vaginal_dick" if_any ["vaginal"]
        always "kleio_carsex_anal_dick" if_any ["anal"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cumshot","vaginal","anal"]
        always "kleio_carsex_vaginal_condom" if_all ["condom","vaginal"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        group khand auto if_any ["hold"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom","vaginal","anal"]


        always "kleio_carsex_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
