init 1:
    layeredimage harmony:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=harmony)


        group position auto


        attribute pubes


        group acc_arm auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless","naked"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group hair auto variant "a" if_any ["a"] if_not ["nun", "sexynun"]:
            attribute up default
        group hair auto variant "b" if_any ["b"] if_not ["nun", "sexynun"]:
            attribute up default
        group hair auto variant "a" if_all ["a", "noacchead"]:
            attribute up default
        group hair auto variant "b" if_all ["b", "noacchead"]:
            attribute up default


        group acc_neck auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["topless","naked"]


        group head auto


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        group stockings auto if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]


        group acc_top auto if_not ["bottomless","naked"]


        attribute noacchead null
        group acc_head auto if_not ["noacchead"]
        group acc_head auto variant "a" if_any ["a"] if_not ["topless","naked", "noacchead"]
        group acc_head auto variant "b" if_any ["b"] if_not ["topless","naked", "noacchead"]


        attribute collar null
        group collar auto if_any ["collar"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage harmony close:
        yalign 0.04
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=harmony)


        group position auto


        attribute pubes


        group acc_arm auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless","naked"]


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        group hair auto variant "a" if_any ["a"] if_not ["nun", "sexynun"]:
            attribute up default
        group hair auto variant "b" if_any ["b"] if_not ["nun", "sexynun"]:
            attribute up default


        group acc_neck auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["topless","naked"]


        group head auto


        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default


        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_a when a
        group multiple auto variant piercings_b when b


        attribute naked null

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant","bottomless","naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless","naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless","naked"]

        group stockings auto if_not ["bottomless","naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant","topless","naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant","topless","naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless","naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless","naked"]


        group acc_top auto if_not ["bottomless","naked"]


        attribute noacchead null
        group acc_head auto if_not ["noacchead"]
        group acc_head auto variant "a" if_any ["a"] if_not ["topless","naked", "noacchead"]
        group acc_head auto variant "b" if_any ["b"] if_not ["topless","naked", "noacchead"]


        attribute collar null
        group collar auto if_any ["collar"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage harmony smartphone:
        always "harmony_smartphone"

    layeredimage harmony kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker], npc=harmony)


        always "harmony_kiss_hair_up" if_not ["halloween", "sexynun"]
        always "harmony_kiss_hair_down" if_any ["halloween", "sexynun"]


        always "harmony_kiss"


        group outfitmike auto if_not ["naked"]:
            attribute normal default


        attribute pregnant


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "naked", "topless"]
        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]


        attribute collar


        group multiple auto variant acc when not naked


        attribute clit null
        attribute tongue null
        attribute navel null
        attribute pregnant_navel null
        group multiple auto variant piercings
        group multiple auto variant piercings_naked when naked or topless

    layeredimage harmony cunnilingus:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker], npc=harmony)


        always "harmony_cunnilingus_bg"


        attribute hairup default if_not ["hairdown"]


        always "harmony_cunnilingus_bodies"


        attribute collar


        attribute pubes


        attribute pregnant


        attribute blush


        group exp auto:
            attribute normal default


        group arms auto:
            attribute pray default


        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_pray when pray
        group multiple auto variant piercings_handjob when handjob


        attribute hairdown


        attribute squirt

    layeredimage harmony missionary:
        attribute_function Pickers([CollarPicker, PubesPicker, PregnancyPicker, PiercingsPicker], npc=harmony)


        group bg auto:
            attribute bedroom default


        always "harmony_missionary_hair" if_not ["nun"]


        always "harmony_missionary_harmony"


        attribute pubes


        attribute pregnant


        attribute tongue null
        group multiple auto variant piercings


        group stockings auto


        group outfit auto if_not ["pregnant"]
        group outfit auto variant "pregnant" if_any ["pregnant"]


        group necklace auto if_not ["collar"]


        attribute noacc null
        group acc_arm auto if_not ["noacc"]


        attribute mike null
        always "harmony_missionary_mike" if_any ["mike"] if_not ["pregnant"]
        always "harmony_missionary_mikepreg" if_all ["mike", "pregnant"]


        attribute cumbody


        attribute blush


        group exp auto:
            attribute normal default


        attribute collar


        group acc_head auto if_not ["noacc"]


        group dick auto if_any "mike":
            attribute outside default


        attribute condom null
        group condom auto if_all ["mike", "condom"] if_not ["condomcum"]


        attribute condomcum null
        group condomcum auto if_all ["mike", "outside", "condomcum"] if_not ["condom"]


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["condom", "outside"]


        attribute cumshot if_all ["mike", "outside"] if_not ["condom"]


        attribute speed

    layeredimage harmony doggy:
        attribute_function Pickers([CollarPicker, PubesPicker, PregnancyPicker, PiercingsPicker], npc=harmony)


        group bg auto:
            attribute bedroom default


        group bodies auto


        group flares auto


        attribute creampie if_not ["condom","out"]


        attribute squirt


        attribute cum null
        group multiple auto variant cum when cum


        attribute pregnant


        group multiple auto variant fx


        group exp auto:
            attribute normal default


        attribute ears null
        attribute tongue null
        group multiple auto variant piercings
        group multiple auto variant piercings_bounce when bounce
        group multiple auto variant piercings_notpreg when not pregnant


        attribute collar


        group hair auto:
            attribute up default


        attribute pov


        group dick auto if_any ["pov"]


        attribute condom null
        group condom auto if_all ["pov","condom"] if_not ["cumshot","creampie"]


        group condomcum auto if_all ["pov","condom"] if_any ["creampie","cumshot"]


        group creampie auto if_all ["pov","creampie"] if_not ["condom"]


        attribute dickcum if_all ["pov","out"] if_not ["condom"]


        attribute cumshot if_all ["pov","out"] if_not ["condom"]

    layeredimage harmony roller:
        group position auto:
            attribute a default

    layeredimage harmony bj:
        attribute_function Pickers([CollarPicker, PubesPicker, PiercingsPicker, PregnancyPicker], npc=harmony)


        group bg auto:
            attribute bedroom default


        always "harmony_bj_body"


        attribute collar


        attribute leash if_any ["collar"]


        attribute pubes


        attribute blush


        group exp auto:
            attribute surprised default
            attribute choke
            attribute orgasm


        group dick auto:
            attribute out default
            attribute suck
            attribute done


        attribute cum null
        group cum auto if_any ["cum"]


        always "harmony_bj_lights"


        attribute pregnant


        group multiple auto variant piercings
        group multiple:
            attribute tongue null

    layeredimage harmony picnic:
        attribute_function SeasonPicker()

        always "harmony_picnic_bg"
        group bg auto

        always "harmony_picnic_characters"

        group fx auto

    layeredimage harmony titjob:
        attribute_function Pickers([DickPicker], npc=harmony)

        always "harmony_titjob_bg"

        attribute blush

        group eyes auto:
            attribute down default
        group mouth auto:
            attribute normal default

        group dick auto

        attribute cum null
        group multiple auto variant cum when cum

        attribute cumshot null
        group cumshot auto if_any ["cumshot"]

    layeredimage harmony church hj:
        attribute_function Pickers([DickPicker, CollarPicker, PiercingsPicker], npc=harmony)


        always "harmony_church_hj_bg"


        always "harmony_church_hj_hairup"


        always "harmony_church_hj_bodies"


        always "harmony_church_hj_back_book"


        attribute speed


        attribute dick null
        group dick auto if_any ["dick"]


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "dick"]


        attribute cumshot null
        group cumshot auto if_all ["cumshot", "dick"]


        group eyes:
            attribute lookmike default
            attribute lookbook


        group mouth:
            attribute surprised default
            attribute happy


        attribute collar


        group multiple auto variant piercings


        always "harmony_church_hj_front_book"

    layeredimage harmony poledance:
        attribute_function Pickers([PubesPicker], npc=harmony)


        always "harmony_poledance_bg"


        if hanna.room == 'stripclub':
            "harmony_poledance_hanna"
        if shiori.room == 'stripclub':
            "harmony_poledance_shiori"


        always "harmony_poledance_mike"


        always "harmony_poledance_harmony"


        attribute pubes


        attribute naked null
        group outfit auto if_not ["naked"]


        group exp auto:
            attribute happy default


        always "harmony_poledance_light"

    layeredimage harmony lapdance:
        attribute_function Pickers([CollarPicker, PiercingsPicker, OutfitPicker, MCCGPicker], npc=harmony)
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
        always "harmony_lapdance_harmony" when not nonpc

        group multiple auto variant piercings when not nonpc

        attribute harmony_naked null
        group outfits auto when not (nonpc or naked or harmony_naked)

        attribute collar when not nonpc

        group exp auto when not nonpc:
            attribute normal default

        group mikeleg auto

        always "harmony_lapdance_fg"
        always "harmony_lapdance_light"

        attribute fuck null
        group fuck auto when fuck and not nonpc

    layeredimage harmony ending beach:
        attribute_function Pickers([EndingKidPicker], npc=harmony)

        always "harmony_ending_beach_bg"
        always "harmony_ending_beach_bodies"
        always "harmony_ending_beach_light"
        attribute kid
        always "harmony_ending_beach_pack"
        always "harmony_ending_beach_fg"

    layeredimage harmony ending church:
        attribute_function Pickers([EndingKidPicker], npc=harmony)

        always "harmony_ending_church_bg"
        always "harmony_ending_church_light"
        attribute kid null
        always "harmony_ending_church_kid" when kid
        always "harmony_ending_church_bodies" when not kid
        always "harmony_ending_church_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
