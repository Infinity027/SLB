init 1:
    layeredimage purity foreplay:
        attribute_function MultiPickers([PiercingsPicker, PubesPicker, CollarPicker, PregnancyPicker, HaircutPicker, DickPicker], npcs=[harmony,reona])


        attribute harmony null
        attribute harmony_clit null
        attribute harmony_tongue null
        attribute reona null
        attribute reona_tongue null
        attribute reona_ears null
        attribute reona_pregnant_navel null
        attribute harmony_pregnant_navel null


        always "purity_foreplay_bg_bedroom"


        always "purity_foreplay_bodies"


        group multiple auto variant pregnancies


        group piercings auto


        always "purity_foreplay_reona_eyes"
        group harmony_eyes auto:
            attribute lookreona default


        group outfits_harmony auto when not harmony_pregnant
        group outfits_harmony auto variant pregnant when harmony_pregnant
        group outfits_reona auto when not reona_pregnant
        group outfits_reona auto variant pregnant when reona_pregnant


        attribute reona_collar
        attribute harmony_collar


        group dick auto


        attribute cumshot null
        group cumshot auto when cumshot


        group hand auto:
            attribute back default


        group multiple auto variant haircuts


        attribute cunni null
        always "purity_foreplay_zoom_cunni" when cunni
        group multiple auto variant zoom when cunni
        group zoom auto variant tongue when cunni:
            attribute down default

    layeredimage purity threesome reona:
        attribute_function MultiPickers([PiercingsPicker, PubesPicker, CollarPicker, PregnancyPicker, HaircutPicker, DickPicker], npcs=[harmony,reona])


        attribute harmony null
        attribute reona null
        attribute harmony_clit null
        attribute harmony_haircut null
        attribute harmony_pubes null
        attribute harmony_tongue null
        attribute reona_clit null
        attribute reona_ears null
        attribute reona_pregnant_navel null
        attribute reona_tongue null


        always "purity_threesome_reona_bg_bedroom"


        always "purity_threesome_reona_bodies"
        attribute bulge
        always "purity_threesome_reona_tattoo"


        group multiple auto variant pregnancies


        group piercings auto


        group harmony_eyes auto:
            attribute lookreona default

        group reona_eyes auto variant nomakeup when reona_nohaircut:
            attribute closed default
        group reona_eyes auto variant makeup when reona_haircut:
            attribute closed default


        attribute reona_collar
        attribute harmony_collar


        group dick auto:
            attribute out default null
        group dick auto variant out when out


        attribute condom null
        group condom auto when condom:
            attribute out null
        group condom auto variant condom_out when condom and out


        attribute cumshot null
        group cumshot auto when cumshot


        attribute creampie
        group creampie auto when creampie


        group harmony_hand auto:
            attribute up default


        group multiple auto variant haircuts

        group fx auto

    layeredimage purity threesome harmony:
        attribute_function MultiPickers([PiercingsPicker, PubesPicker, CollarPicker, PregnancyPicker, HaircutPicker, DickPicker], npcs=[harmony,reona])


        attribute harmony null
        attribute reona null
        attribute harmony_clit null
        attribute harmony_navel null
        attribute harmony_nipples null
        attribute harmony_nohaircut null
        attribute harmony_pubes null
        attribute harmony_tongue null
        attribute reona_ears null
        attribute reona_pregnant_navel null
        attribute reona_tongue null


        always "purity_threesome_harmony_bg_bedroom"


        always "purity_threesome_harmony_bodies"
        always "purity_threesome_harmony_reona_tattoo_belly"
        always "purity_threesome_harmony_reona_tattoo_face" when reona_nohaircut


        group multiple auto variant pregnancies


        group piercings auto


        group harmony_eyes auto:
            attribute back default


        group reona_mouth auto:
            attribute oo default

        group harmony_mouth auto:
            attribute half default
        attribute tongue


        attribute makeup null
        always "purity_threesome_harmony_reona_eyes" when reona_haircut
        always "purity_threesome_harmony_reona_makeup_eyes" when reona_nohaircut
        group reona_makeup_mouth auto when reona_nohaircut


        attribute reona_collar
        attribute harmony_collar


        group dick auto
        group dick auto variant out when not (vaginal or anal)

        attribute condom null
        group condom auto when condom:
            attribute out null
        group condom auto variant out when condom and out


        attribute cum
        attribute cumshot null
        group cumshot auto when cumshot


        attribute creampie null
        group creampie auto when creampie


        always "purity_threesome_harmony_mike_hands_right"
        group mike_hands auto variant left:
            attribute thigh default


        group multiple auto variant haircuts


        attribute squirt
        attribute speed

    layeredimage purity ending:
        attribute_function MultiPickers([HaircutPicker, EndingKidPicker], npcs=[harmony,reona])

        always "purity_ending_bg"
        group multiple auto variant kids
        attribute harmony
        attribute reona
        group multiple auto variant haircuts
        group multiple:
            attribute harmony_nohaircut null
            attribute harmony_haircut null
        always "purity_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
