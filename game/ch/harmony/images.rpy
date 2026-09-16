init 1:
    layeredimage harmony:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=harmony)

        group position auto

        attribute pubes

        group acc_arm auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless","naked"]

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
  
        attribute naked null

        attribute bottomless null

        group stockings auto if_not ["bottomless","naked"]

        attribute topless null

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
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=harmony)

        group position auto

        attribute pubes

        group acc_arm auto variant "a" if_any ["a"] if_not ["topless","naked"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["topless","naked"]


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
        attribute naked null

        attribute bottomless null

        group stockings auto if_not ["bottomless","naked"]

        attribute topless null

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

    layeredimage harmony roller:
        group position auto:
            attribute a default

    layeredimage harmony picnic:
        attribute_function SeasonPicker()

        always "harmony_picnic_bg"
        group bg auto

        always "harmony_picnic_characters"

        group fx auto

    layeredimage harmony church hj:
        attribute_function Pickers([DickPicker, CollarPicker], npc=harmony)

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
        attribute_function Pickers([CollarPicker,  OutfitPicker, MCCGPicker], npc=harmony)
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
