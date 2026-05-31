init 1:
    layeredimage petite 4some cumshare:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, DickPicker], npcs=[anna,emma,kat])


        group bg auto:
            attribute bedroom default


        attribute emma null
        always "petite_4some_cumshare_emma"
        attribute emma_nose
        attribute emma_clit null
        attribute emma_lips null
        attribute emma_navel null
        attribute emma_nipples null
        attribute emma_tongue null
        attribute emma_collar
        group emma_mouths auto:
            attribute emma_mouth_open default
        group emma_eyes auto:
            attribute emma_eyes_open default
        always "petite_4some_cumshare_emma_shadow"


        attribute kat null
        always "petite_4some_cumshare_kat_nohaircut" if_not ["kat_haircut"]
        attribute kat_haircut
        attribute kat_nose
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_nipples null
        attribute kat_tongue null
        attribute kat_collar
        group kat_mouths auto:
            attribute kat_mouth_open default
        group kat_eyes auto:
            attribute kat_eyes_open default
        attribute kathand


        attribute anna null
        always "petite_4some_cumshare_anna"
        attribute anna_nose
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        attribute anna_collar
        group anna_mouths auto:
            attribute anna_mouth_open default
        group anna_eyes auto:
            attribute anna_eyes_open default
        attribute annahand


        group multiple auto variant facecum


        group multiple auto variant fx


        attribute cum null
        group cum auto if_any ["cum"]
        group dick auto
        attribute throb null
        group throb auto if_any ["throb"]

    layeredimage petite 4some foreplay:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, DickPicker], npcs=[anna], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        always "petite_4some_foreplay_bodies"
        attribute anna null
        attribute anna_pregnant
        attribute anna_nose
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        group dick auto


        attribute emmahand if_any ["emma"]
        attribute emma "petite_4some_foreplay_emma1"
        attribute emma_pregnant if_any ["emma"]
        attribute emma_collar if_any ["emma"]
        attribute emma_nose if_any ["emma"]
        attribute emma_nipples if_any ["emma"]
        attribute emma_clit null
        attribute emma_lips null
        attribute emma_tongue null
        attribute emma_navel if_any ["emma"]
        attribute emma "petite_4some_foreplay_emma2"


        attribute kat "petite_4some_foreplay_kat1"
        attribute kat_pregnant if_any ["kat"]
        attribute kat_collar if_any ["kat"]
        attribute kat_nipples if_any ["kat"]
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_tongue null
        attribute kat_nose if_any ["kat"]
        attribute kat "petite_4some_foreplay_kat2"
        always "petite_4some_foreplay_kat_nohaircut" if_any ["kat"] if_not ["kat_haircut"]
        attribute kat_haircut if_any ["kat"]

    layeredimage petite 4some fuckall:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker], append_npc_from_attributes=True)


        group bg auto:
            attribute bedroom default


        attribute anna
        attribute anna_pregnant if_any ["anna"]
        attribute anna_nose if_any ["anna"]
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_navel null
        attribute anna_nipples null
        attribute anna_tongue null
        group anna_mouths auto if_any ["anna"]:
            attribute anna_mouth_smile default
        group anna_eyes auto if_any ["anna"]:
            attribute anna_eyes_open default
        attribute bodycum_anna if_any ["anna"]


        attribute emma
        attribute emma_pregnant if_any ["emma"]
        attribute emma_nose if_any ["emma"]
        attribute emma_clit null
        attribute emma_lips null
        attribute emma_navel null
        attribute emma_nipples null
        attribute emma_tongue null
        group emma_mouths auto if_any ["emma"]:
            attribute emma_mouth_happy default
        group emma_eyes auto if_any ["emma"]:
            attribute emma_eyes_open default
        attribute bodycum_emma if_any ["emma"]


        attribute kat
        attribute kat_haircut if_any ["kat"]
        always "petite_4some_fuckall_kat_nohaircut" if_any ["kat"] if_not ["kat_haircut"]
        attribute kat_pregnant if_any ["kat"]
        attribute kat_nose if_any ["kat"]
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_nipples null
        attribute kat_tongue null
        group kat_mouths auto if_any ["kat"]:
            attribute kat_mouth_smile default
        group kat_eyes auto if_any ["kat"]:
            attribute kat_eyes_open default
        attribute bodycum_kat if_any ["kat"]


        attribute dickonly null
        group dick auto if_any ["mike"]
        group dick_vaginal auto if_all ["vaginal"] if_any ["mike", "dickonly"]
        group dick_anal auto if_all ["anal"] if_any ["mike", "dickonly"]


        attribute condom null
        group condom_vaginal auto if_all ["condom", "vaginal"] if_any ["mike", "dickonly"]


        attribute cum null
        group cum auto if_all ["mike", "cum"]
        group cum_vaginal auto if_all ["cum", "vaginal"] if_any ["mike", "dickonly"] if_not ["condom"]
        group cum_anal auto if_all ["cum", "anal"] if_any ["mike", "dickonly"]


        attribute hand null
        group hand auto if_all ["mike", "hand"]


        attribute mike null
        group mike if_any ["mike"]:
            attribute behind_emma default
            attribute behind_anna
            attribute behind_kat
        group mike if_any ["mike"] if_not ["dickonly"]:
            attribute fuck_emma
            attribute fuck_anna
            attribute fuck_kat
        group mike_inside:
            attribute vaginal null default
            attribute anal null

    layeredimage petite 4some fuckanna:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npcs=[anna,emma,kat])


        attribute anna null
        attribute anna_clit null
        attribute anna_ears null
        attribute anna_navel null
        attribute anna_nipples null
        attribute anna_nose null
        attribute anna_tongue null
        attribute anna_pubes null
        attribute emma null
        attribute emma_lips null
        attribute emma_tongue null
        attribute emma_pubes null
        attribute kat null
        attribute kat_ears null
        attribute kat_nipples null
        attribute kat_tongue null


        group bg auto:
            attribute bedroom default


        always "petite_4some_fuckanna_girls"


        attribute bodycum


        group multiple auto variant pubic
        group multiple auto variant pregnancy
        group multiple auto variant piercings
        group multiple auto variant collars


        group exp auto:
            attribute anna_lookfront default


        always "petite_4some_fuckanna_faceandhair"


        attribute kat_haircut
        always "petite_4some_fuckanna_kat_nohaircut" if_not ["kat_haircut"]


        attribute mike


        group dick auto if_any ["mike"]:
            attribute out null default
        group dick auto variant "out" if_all ["mike", "out"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "condom", "out"]


        attribute cum null
        group cum auto if_all ["mike", "cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["mike", "cum", "out"] if_not ["condom"]


        group fg auto

    layeredimage petite 4some fuckemma:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, PiercingsPicker, CollarPicker, DickPicker], npcs=[anna,emma,kat])


        attribute anna null
        attribute anna_ears null
        attribute anna_tongue null
        attribute emma null
        attribute emma_lips null
        attribute emma_tongue null
        attribute kat null
        attribute kat_clit null
        attribute kat_ears null
        attribute kat_navel null
        attribute kat_nose null
        attribute kat_tongue null
        attribute kat_pubes null


        group bg auto:
            attribute bedroom default





        always "petite_4some_fuckemma_emma"
        attribute emma_nipples
        attribute emma_navel
        attribute emma_nose
        attribute emma_collar
        attribute emma_pubes
        group exp_emma auto:
            attribute emma_normal default
        always "petite_4some_fuckemma_emmahair"


        always "petite_4some_fuckemma_anna"
        attribute anna_pubes
        attribute anna_clit
        attribute anna_nose
        attribute anna_nipples
        attribute anna_navel
        attribute anna_collar
        always "petite_4some_fuckemma_annaface"


        always "petite_4some_fuckemma_kat"
        attribute kat_nipples
        attribute kat_collar
        attribute kat_haircut
        always "petite_4some_fuckemma_kat_nohaircut"if_not ["kat_haircut"]
        always "petite_4some_fuckemma_katface"


        attribute anna_pregnant
        attribute anna_pregnant_navel
        attribute kat_pregnant
        attribute emma_pregnant
        attribute emma_pregnant_navel


        attribute bodycum


        attribute mike


        group dick auto if_any ["mike"]:
            attribute out null default
        attribute cum null
        group cum auto if_all ["mike", "cum"] if_not ["condom"]
        attribute condom null
        group condom auto if_all ["mike", "condom"]


        always "petite_4some_fuckemma_annahand"
        attribute openpussy if_not ["vaginal"]
        attribute vaginaldrip if_any ["openpussy"] if_not ["vaginal"]
        attribute emma_clit
        always "petite_4some_fuckemma_kathand"
        always "petite_4some_fuckemma_emmahand"


        group dick auto variant "out" if_all ["mike", "out"]
        group cum auto variant "out" if_all ["mike", "out", "cum"] if_not ["condom"]
        group condom auto variant "out" if_all ["mike", "out", "condom"]

    layeredimage petite 4some fuckkat:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, PiercingsPicker, CollarPicker], npcs=[kat], append_npc_from_attributes=True)


        attribute anna_clit null
        attribute anna_ears null
        attribute anna_navel null
        attribute anna_nose null
        attribute anna_tongue null
        attribute emma_clit null
        attribute emma_lips null
        attribute emma_navel null
        attribute emma_tongue null
        attribute emma_pubes null
        attribute kat null
        attribute kat_ears null
        attribute kat_tongue null


        group bg auto:
            attribute bedroom default


        always "petite_4some_fuckkat_emmahand" if_any ["emma"]


        always "petite_4some_fuckkat_kat"
        attribute kat_pubes
        attribute kat_pregnant
        attribute kat_pregnant_navel
        attribute kat_navel
        attribute kat_nose
        attribute kat_clit
        attribute kat_nipples
        attribute kat_collar
        attribute kat_blush
        group exp_kat auto:
            attribute kat_normal default
        attribute kat_haircut
        always "petite_4some_fuckkat_kat_nohaircut" if_not ["kat_haircut"]


        attribute emma
        attribute emma_pregnant if_any ["emma"]
        attribute emma_nose if_any ["emma"]
        attribute emma_nipples if_any ["emma"]
        always "petite_4some_fuckkat_emmaface" if_any ["emma"]
        attribute emma_collar if_any ["emma"]


        attribute anna
        attribute anna_collar if_any ["anna"]
        attribute anna_nipples if_any ["anna"]
        attribute anna_pubes if_any ["anna"]
        attribute anna_pregnant if_any ["anna"]
        always "petite_4some_fuckkat_annaface" if_any ["anna"]


        group dick auto:
            attribute out default
        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        attribute condom null
        group condom auto if_any ["condom"]


        group fg auto

    layeredimage petite ending:
        attribute_function MultiPickers([HaircutPicker, EndingKidPicker], npcs=[anna, emma, kat])
        always "petite_ending_bg"
        always "petite_ending_mike"
        attribute anna_kid
        always "petite_ending_kat"
        group haircuts auto
        attribute kat_kid
        always "petite_ending_anna"
        always "petite_ending_emma"
        attribute emma_kid
        always "petite_ending_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
