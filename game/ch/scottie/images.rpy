init 1:
    layeredimage scottie:
        attribute_function Pickers([PositionPicker, OutfitPicker, PiercingsPicker], npc=scottie)


        group position auto:
            attribute a default

        always:
            if_all ["naked"]
            "scottie_dick"
        group multiple auto variant piercings
        group piercings auto variant "b" if_any "b"


        group outfit auto variant "a" if_any "a":
            attribute naked null
        group outfit auto variant "b" if_any "b":
            attribute naked null

        group exp auto:
            attribute normal default null

        group multiple auto variant acc

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage scottie close:
        yalign 0.05
        attribute_function Pickers([PositionPicker, OutfitPicker, PiercingsPicker], npc=scottie)


        group position auto:
            attribute a default

        always:
            if_all ["naked"]
            "scottie_close_dick"
        group multiple auto variant piercings
        group piercings auto variant "b" if_any "b"


        group outfit auto variant "a" if_any "a":
            attribute naked null
        group outfit auto variant "b" if_any "b":
            attribute naked null

        group exp auto:
            attribute normal default null

        group multiple auto variant acc

        group arm auto
        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage scottie smartphone:
        always "scottie_smartphone"

    layeredimage scottie 2hj:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PubesPicker, HaircutPicker], npc=sasha)

        always:
            "scottie_2hj_bg"

        always:
            "scottie_2hj_sasha"

        attribute boobjob
        attribute collar
        attribute haircut
        attribute pubes

        attribute blur

        always:
            "scottie_2hj_mike"

        always:
            "scottie_2hj_scottie"



        group multiple auto variant piercings
        group piercings auto variant "boobjob" if_any "boobjob"
        group piercings auto variant "noboobjob" if_not "boobjob"

        group mouth auto:
            attribute shut default
        group eyes auto:
            attribute ahead default

        group multiple auto variant cum

    layeredimage scottie dp:
        attribute_function Pickers([PiercingsPicker, CollarPicker, HaircutPicker, PregnancyPicker], npc=sasha)

        attribute bottom null
        attribute bottomcondom null
        attribute bottomcum null
        attribute top null
        attribute topcondom null
        attribute topcum null

        always:
            "scottie_dp_bg"

        group bottomhead auto if_all "bottom"

        always:
            "scottie_dp_sasha"

        attribute haircut
        attribute collar
        attribute pregnant
        attribute boobjob

        group multiple auto variant piercings
        group piercings auto variant "boobjob" if_any "boobjob"
        group piercings auto variant "noboobjob" if_not "boobjob"

        group exp auto:
            attribute normal default

        group bottom auto if_all "bottom"
        group bottomdick variant "scottietop" auto if_all ["scottietop","bottom"]:
            attribute bottomnodick null
            attribute bottomout default
        group bottomdick variant "miketop" auto if_all ["miketop","bottom"]:
            attribute bottomnodick null
            attribute bottomout default
        group bottomcondom auto if_all ["bottom","bottomcondom"]
        group multiple auto variant bottomcum when bottom and bottomcum and not bottomcondom

        group top auto if_all "top"
        group tophair auto if_all "top"
        group topdick auto if_all "top":
            attribute topnodick null
            attribute topout default
        group topcondom auto if_all ["top","topcondom"]
        group multiple auto variant topcum when top and topcum and not topcondom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
