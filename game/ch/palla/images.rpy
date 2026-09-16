init 1:
    layeredimage palla:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=palla)

        attribute idle null

        group hair_bg auto if_not ["halloween"]

        group position auto


        attribute blush

        group hair_fg auto if_not ["halloween"]
        group hair_fg auto variant "halloween" if_any ["halloween"]

        attribute collar null
        group collar auto if_any ["collar"]

        group exp auto:
            attribute normal default

        attribute tongue null
        attribute lips null

        attribute pubes

        attribute naked null

        attribute topless null

        attribute bottomless null
    
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
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=palla)

        attribute idle null

        group hair_bg auto if_not ["halloween"]

        group position auto

        attribute blush

        group hair_fg auto if_not ["halloween"]
        group hair_fg auto variant "halloween" if_any ["halloween"]

        attribute collar null
        group collar auto if_any ["collar"]

        group exp auto:
            attribute normal default

        attribute tongue null
        attribute lips null

        attribute pubes

        attribute naked null

        attribute topless null

        attribute bottomless null

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

    layeredimage palla restaurantbj:

        always "palla_restaurantbj_bg"

        group body auto:
            attribute kissdick default

        group cum auto if_any ['kissdick', 'suckdick']

    layeredimage palla pornstar ending:
        attribute_function Pickers([CollarPicker], npc=palla)

        always "palla_pornstar_ending_bg"

        always "palla_pornstar_ending_bodies"

        attribute collar

        always "palla_pornstar_ending_mike"

        attribute naked null
        always "palla_pornstar_ending_mike_casual" if_not ["naked"]

    layeredimage palla model ending:
        attribute_function Pickers([CollarPicker], npc=palla)

        always "palla_model_ending_bg"

        always "palla_model_ending_palla"

        attribute naked null

        always "palla_model_ending_fashion" if_not ["naked"]

        always "palla_model_ending_pregnant_fashion" if_any ["pregnant"] if_not ["naked"]

        attribute collar

        always "palla_model_ending_glasses" if_not ["naked"]

        always "palla_model_ending_mike"

    layeredimage palla dogeza:

        always "palla_dogeza_bg"

        always "palla_dogeza_palla"

        always "palla_dogeza_clothes"
        group underwear auto:
            attribute worn default
