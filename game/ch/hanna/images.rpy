init 1:
    layeredimage hanna:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, ArmpitsPicker, PubesPicker], npc=hanna)


        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings:
            attribute clit when naked or bottomless
        group multiple auto variant piercings_flirt when flirt
        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_mindless when mindless


        attribute armpits null
        group armpits auto if_any "armpits"


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]

        group jacket auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group jacket auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group jacket auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group jacket auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]

        attribute sweat null
        group sweat auto if_any ["sweat"]


        attribute collar


        group multiple auto variant acc
        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        group arm auto


        group hat auto

    layeredimage hanna close:
        yalign 0.05
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, ArmpitsPicker, PubesPicker], npc=hanna)


        group position auto

        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        group exp auto:
            attribute normal default


        group multiple auto variant piercings:
            attribute clit when naked or bottomless
        group multiple auto variant piercings_flirt when flirt
        group multiple auto variant piercings_surprised when surprised
        group multiple auto variant piercings_mindless when mindless


        attribute armpits null
        group armpits auto if_any "armpits"


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]

        group jacket auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group jacket auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group jacket auto variant "a_pregnant" if_all ["a","pregnant"] if_not ["topless","naked"]
        group jacket auto variant "b_pregnant" if_all ["b","pregnant"] if_not ["topless","naked"]

        attribute sweat null
        group sweat auto if_any ["sweat"]


        attribute collar


        group multiple auto variant acc
        group multiple auto variant acc_a when a
        group multiple auto variant acc_b when b


        group arm auto


        group hat auto

    layeredimage hanna smartphone:
        always "hanna_smartphone"

    layeredimage hanna mast:

        always "hanna_mast_bg"
        always "hanna_mast_body"

        group exp auto:
            attribute a default

        attribute outfit:
            "hanna_mast_top"
        attribute outfit:
            "hanna_mast_bot"

        attribute squirt
        attribute wet

        always "hanna_mast_light"

    layeredimage hanna bj:
        attribute_function Pickers([PiercingsPicker], npc=hanna)

        always "hanna_bj_bg"
        always "hanna_bj_body"

        group face auto:
            attribute normal default
        group exp auto variant "suck" if_any ["suck"]:
            attribute open default
        group exp auto variant "normal" if_any ["normal"]:
            attribute open default

        group dick auto:
            attribute b default

        attribute nose null
        group nose auto if_any ["nose"]
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a

        attribute outfit

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

        attribute bodycum

        attribute wet null
        group wet auto if_any ["wet"]

        always "hanna_bj_water_fx"

        always "hanna_bj_man"

    layeredimage hanna cowgirl:
        attribute_function Pickers([PregnancyPicker], npc=hanna)

        attribute armpits null

        group bg auto:
            attribute bedroom default

        always "hanna_cowgirl_man"
        always "hanna_cowgirl_dick"

        attribute wet if_any ["up"]:
            "hanna_cowgirl_wet"

        attribute cum

        group fuck auto:
            attribute up default

        attribute pregnant
        always "hanna_cowgirl_body"

        group exp auto:
            attribute smile default
        group boob auto:
            attribute normal default

        attribute wet if_any ["down"]:
            "hanna_cowgirl_splash"

        group multiple auto variant fx

    layeredimage hanna kiss:
        attribute_function Pickers([OutfitPicker], npc=hanna)


        always "hanna_kiss_bodies"

        attribute armpits


        group mikeoutfit auto if_not ["naked"]:
            attribute normal default


        attribute acc default if_any ["wedding"] if_not ["naked"]


        attribute naked null
        attribute topless null
        group outfit auto if_not ["naked", "topless"]


        group hat auto if_not ["naked", "topless"]

    layeredimage hanna missionary:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=hanna)


        always "hanna_missionary_bg"


        always "hanna_missionary_body"

        group hands auto:
            attribute up default

        attribute armpits null
        group armpits auto if_any "armpits"


        group exp auto:
            attribute normal default
            attribute fuck
            attribute orgasm
            attribute ahegao


        attribute blush


        attribute speed if_any ["down"]


        group multiple auto variant fx 


        attribute pregnant


        attribute collar


        group multiple auto variant piercings


        group outfit auto


        group hat auto


        group mike:
            attribute sex default
            attribute oral


        group dick auto:
            attribute out default
            attribute pussy
            attribute ass


        attribute condom null
        group condom auto if_any ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        attribute night

    layeredimage hanna doggy:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker, CollarPicker], npc=hanna)


        group bg auto:
            attribute bedroom default

        group mat auto

        always "hanna_doggy_hanna"

        attribute armpits


        attribute blush


        group exp auto:
            attribute normal default
            attribute happy
            attribute ahegao


        attribute pregnant


        group multiple auto variant piercings
        group multiple:
            attribute nipples null
            attribute tongue null
        group multiple auto variant piercings_default when not vaginal
        group multiple auto variant piercings_vaginal when vaginal

        group acc auto

        attribute collar
        attribute leash

        attribute sweat

        attribute pubes


        attribute mike


        group fuck auto if_all ["mike"] if_any ["anal", "vaginal"]
        group outside auto if_all ["mike"] if_not ["anal", "vaginal"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["condom", "mike", "vaginal"]
        group condom_outside auto if_all ["condom", "mike"] if_not ["vaginal", "anal"]

        always "hanna_doggy_balls_outside" if_all ["mike"] if_not ["anal", "vaginal"]

        attribute squirt

        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal", "anal"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["vaginal", "anal"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["condom", "vaginal", "anal"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]

        group lights auto

    layeredimage hanna stand:
        attribute_function Pickers([PiercingsPicker, CollarPicker, PregnancyPicker], npc=hanna)


        group bg auto:
            attribute house default


        always "hanna_stand_bodies"


        attribute collar


        group multiple auto variant piercings


        attribute naked null
        always "hanna_stand_outfit_mike" if_not ["naked"]
        always "hanna_stand_outfit_hanna" if_not ["naked"]


        attribute pregnant if_all ["pregnant", "naked"]
        always "hanna_stand_pregnant_outfit" if_any ["pregnant"] if_not ["naked"]


        group fg auto

    layeredimage hanna lapdance:
        attribute_function Pickers([OutfitPicker, PubesPicker, CollarPicker, PiercingsPicker, MCCGPicker], npc=hanna)

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
        always "hanna_lapdance_hanna" when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        group multiple auto variant piercings when not nonpc
        group multiple:
            attribute nose null
            attribute tongue null

        attribute pubes when not nonpc
        attribute armpits when not nonpc

        attribute hanna_naked null
        group outfits auto when not (nonpc or naked or hanna_naked)

        attribute collar when not nonpc

        always "hanna_lapdance_fg"
        always "hanna_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage hanna gym ending:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, EndingKidPicker], npc=hanna)
        always:
            "hanna_gym_ending_bg"

        always:
            "hanna_gym_ending_mike"

        attribute pregnant null

        attribute kid

        always:
            "hanna_gym_ending_hanna"

        attribute collar

        group multiple auto variant piercings

        always:
            "hanna_gym_ending_sexywork"

        always:
            "hanna_gym_ending_fg"

    layeredimage hanna house ending:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker, EndingKidPicker], npc=hanna)
        always:
            "hanna_house_ending_bg"

        always:
            "hanna_house_ending_mike"

        attribute pregnant null

        always:
            "hanna_house_ending_hanna"

        attribute kid
        always:
            if_any "kid"
            "hanna_house_ending_casual"

        always:
            "hanna_house_ending_apron"

        attribute collar

        group multiple auto variant piercings

        always:
            "hanna_house_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
