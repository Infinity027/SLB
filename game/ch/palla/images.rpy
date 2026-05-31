init 1:
    layeredimage palla:
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=palla)


        attribute idle null


        group hair_bg auto if_not ["halloween"]


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        attribute blush


        group hair_fg auto if_not ["halloween"]
        group hair_fg auto variant "halloween" if_any ["halloween"]


        attribute collar null
        group collar auto if_any ["collar"]


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings
        group multiple auto variant piercings_lips when lips


        attribute pubes


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]


        group pregnant auto variant "halloween" if_all ["pregnant", "halloween"]


        attribute noacc null
        group multiple auto variant acc when not (noacc or naked)
        group multiple auto variant acc_a when a and not (noacc or naked)
        group multiple auto variant acc_b when b and not (noacc or naked)
        attribute facecum


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage palla close:
        yalign 0.04
        attribute_function Pickers([PositionPicker, PiercingsPicker, PregnancyPicker, CollarPicker, PubesPicker, OutfitPicker], npc=palla)


        attribute idle null


        group hair_bg auto if_not ["halloween"]


        group position auto


        attribute pregnant null
        group pregnant auto if_any ["pregnant"] if_not ["halloween"]


        attribute blush


        group hair_fg auto if_not ["halloween"]
        group hair_fg auto variant "halloween" if_any ["halloween"]


        attribute collar null
        group collar auto if_any ["collar"]


        group exp auto:
            attribute normal default


        attribute tongue null
        attribute lips null
        group multiple auto variant piercings
        group multiple auto variant piercings_lips when lips


        attribute pubes


        attribute naked null

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group poke_piercings auto variant a when a and nipples and not (topless or naked)
        group poke_piercings auto variant b when b and nipples and not (topless or naked)

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]


        group pregnant auto variant "halloween" if_all ["pregnant", "halloween"]


        attribute noacc null
        group multiple auto variant acc when not (noacc or naked)
        group multiple auto variant acc_a when a and not (noacc or naked)
        group multiple auto variant acc_b when b and not (noacc or naked)
        attribute facecum


        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage palla smartphone:
        always "palla_smartphone"

    layeredimage palla spank:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker], npc=palla)

        attribute glasses null


        always "palla_spank_bg"


        always "palla_spank_bodies"


        attribute marks


        group exp auto:
            attribute normal default



        attribute topless null
        group outfit_top auto if_not ["topless"]:
            attribute naked null
        attribute bottomless null
        group outfit_bot auto if_not ["bottomless", "down"]:
            attribute naked null
        attribute down null
        group outfit_bot auto variant "down" if_any ["down"] if_not ["bottomless"]:
            attribute naked null


        attribute collar


        group multiple auto variant piercings
        group multiple auto variant piercings_surprised when surprised


        group arm auto:
            attribute middle default


        group fx auto

    layeredimage palla stand:
        attribute_function Pickers([PregnancyPicker, PubesPicker, CollarPicker, PiercingsPicker], npc=palla)

        group position auto:
            attribute other null default
            attribute balcony null


        attribute nobg
        group bg auto if_not ["nobg"]:
            attribute cabin default


        group bodies auto
        attribute pubes


        group hair_base auto when not halloween

        group mike_arm auto


        group outfit auto when other


        attribute cumscreen


        group collars auto variant other when other
        group collars auto variant balcony when balcony


        attribute pregnant null
        group pregnant auto variant other when pregnant and other:
            attribute naked default

        group pregnant auto variant balcony when pregnant and balcony


        group exp auto variant other when other:
            attribute normal default
        group exp auto variant balcony when balcony


        group dick auto:
            attribute nodick default null


        attribute cum null
        group cum auto if_any ["cum"]


        attribute wet null
        group wet auto if_any ["wet"]


        group multiple auto variant piercings_other when other
        group multiple auto variant piercings_other_smile when other and smile
        group multiple auto variant piercings_other_pleasure when other and pleasure

        group multiple auto variant piercings_balcony when balcony


        group hair_halloween auto when halloween


        group fg auto

    layeredimage palla doggy:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, PregnancyPicker], npc=palla)

        group bg auto:
            attribute bedroom1 default
        always "palla_doggy_shadow"
        always "palla_doggy_body"

        group exp auto:
            attribute normal default

        attribute pregnant

        group multiple auto variant piercings_normal when normal and not (orgasm or ahegao)
        group multiple auto variant piercings_orgasm when orgasm and not (normal or ahegao)
        group multiple auto variant piercings_ahegao when ahegao and not (orgasm or normal)

        attribute sweat

    layeredimage palla restaurantbj:

        always "palla_restaurantbj_bg"

        group body auto:
            attribute kissdick default

        group cum auto if_any ['kissdick', 'suckdick']

    layeredimage palla kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker], npc=palla)



        always "palla_kiss"




        group multiple:
            attribute clit null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null
            attribute nose null
            attribute tongue null
        group multiple auto variant piercings_naked


        attribute naked null
        attribute topless null
        group outfit auto if_not ["pregnant", "naked", "topless"]
        attribute collar
        group multiple auto variant piercings


        group hairs auto:
            attribute usual default


        group outfitmike auto if_not ["naked"]:
            attribute normal default


        attribute pregnant


        group outfit auto variant "pregnant" if_any ["pregnant"] if_not ["naked", "topless"]



        attribute glasses

    layeredimage palla missionary:
        attribute_function Pickers([PubesPicker, PiercingsPicker, PregnancyPicker, CollarPicker, OutfitPicker, MCCGPicker], npc=palla)

        attribute nobg null
        group bg auto when not nobg:
            attribute bedroom1 default

        always "palla_missionary_palla"
        always "palla_missionary_hairs"
        always "palla_missionary_vaginal_closed" when not vaginal

        attribute pubes

        attribute pregnant

        attribute collar

        attribute naked null
        group outfit auto when not naked and not pregnant
        group outfit auto variant pregnant when pregnant and not naked

        group exp auto:
            attribute normal default

        group multiple auto variant piercings

        attribute nomc null
        attribute mikemc when not nomc
        always "palla_missionary_testicules" when not nomc

        group dick_position auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant out when out and not nomc
        group dick auto variant vaginal when vaginal and not nomc
        group dick auto variant anal when anal and not nomc

        attribute condom null
        group condom auto variant out when out and condom and not nomc
        group condom auto variant vaginal when vaginal and condom and not nomc

        attribute cumshot null
        group cumshot auto variant out when cumshot and out and not nomc and not condom
        group cumshot auto variant vaginal when cumshot and vaginal and not nomc and not condom
        group cumshot auto variant anal when cumshot and anal and not nomc

        attribute cum null
        group multiple auto variant cum when cum and not nomc and not condom

        attribute mc_underwear when not naked

    layeredimage palla cowgirl:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker, CollarPicker], npc=palla)

        always "palla_cowgirl_bg"
        always "palla_cowgirl_palla"

        group exp auto:
            attribute pain default

        attribute collar

        attribute pregnant

        group dick auto:
            attribute outside default
            attribute after "palla_cowgirl_dick_outside"
            attribute condom "palla_cowgirl_dick_vaginal"

        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]

        attribute condom

        group multiple auto variant piercings
        group multiple auto variant piercings_normal when not ahegao
        group multiple auto variant piercings_ahegao when ahegao

    layeredimage palla pornstar ending:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=palla)

        always "palla_pornstar_ending_bg"

        always "palla_pornstar_ending_bodies"

        attribute pregnant

        attribute collar

        group multiple auto variant piercings

        always "palla_pornstar_ending_mike"

        attribute naked null
        always "palla_pornstar_ending_mike_casual" if_not ["naked"]

    layeredimage palla model ending:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=palla)

        always "palla_model_ending_bg"

        always "palla_model_ending_palla"

        attribute pregnant

        group multiple auto variant piercings when naked

        attribute naked null

        always "palla_model_ending_fashion" if_not ["naked"]

        always "palla_model_ending_pregnant_fashion" if_any ["pregnant"] if_not ["naked"]

        attribute collar

        group multiple auto variant piercings_front

        always "palla_model_ending_glasses" if_not ["naked"]

        always "palla_model_ending_mike"

    layeredimage palla dogeza:

        always "palla_dogeza_bg"


        always "palla_dogeza_palla"


        always "palla_dogeza_clothes"
        group underwear auto:
            attribute worn default

    layeredimage palla blowjob:
        attribute_function Pickers([PiercingsPicker, CollarPicker, OutfitPicker, DickPicker], npc=palla)


        attribute casual null
        attribute hero_casual null
        attribute date null
        attribute hero_date null


        group bg auto:
            attribute bedroom1 default


        always "palla_blowjob_malehero"
        group dick auto
        always "palla_blowjob_hero_hand"


        always "palla_blowjob_palla"
        attribute finger null
        always "palla_blowjob_nofinger" if_not ["finger"]
        group exp auto:
            attribute normal default


        attribute collar


        group multiple auto variant piercings:
            attribute tongue null
            attribute navel null
            attribute pregnant_navel null
            attribute clit null


        attribute naked null
        attribute underwear if_not ["naked"]
        attribute noglasses null
        attribute glasses if_not ["noglasses"]


        attribute cum null
        group cum auto if_any ["cum"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
