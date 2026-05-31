init 1:
    layeredimage bree kat cowgirl:
        attribute_function Pickers([DickPicker, PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker], npc=bree)


        always "bree_kat_cowgirl_bg"
        always "bree_kat_cowgirl_bodies"


        attribute bree_pubes


        attribute pregnant


        attribute collar


        always "bree_kat_cowgirl_katface"
        group exp auto:
            attribute pleasure default


        group multiple auto variant piercings


        attribute bodycum


        group fckpos:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto
        attribute condom null
        group condom auto if_any ["condom"]
        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group dick auto variant "out" if_any ["out"]
        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]

    layeredimage bree kat rev cowgirl:
        attribute_function Pickers([DickPicker, PiercingsPicker, CollarPicker], npc=bree)


        always "bree_kat_rev_cowgirl_bg"
        always "bree_kat_rev_cowgirl_bodies"


        attribute collar


        group multiple auto variant piercings


        attribute bodycum


        always "bree_kat_rev_cowgirl_bree_face"
        group exp auto:
            attribute normal default


        group fckpos:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto
        attribute condom null
        group condom auto if_any ["condom"]
        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        group dick auto variant "out" if_any ["out"]
        group condom auto variant "out" if_all ["out", "condom"] if_not ["cumshot"]
        group condomcum auto if_all ["out", "condom", "cumshot"]
        attribute cumshot null
        group cumshot auto if_all ["out", "cumshot"] if_not ["condom"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
