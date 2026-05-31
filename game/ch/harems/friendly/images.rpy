init 1:
    layeredimage friendly harem bj:
        attribute_function MultiPickers([DickPicker, PiercingsPicker, PubesPicker, CollarPicker], npcs=[samantha], append_npc_from_attributes=True)

        attribute samantha default
        attribute emma null

        always "friendly_harem_bj_bg"
        always "friendly_harem_bj_bodies"

        group collars auto

        group hands auto if_not "samhj"
        group mouth auto if_not "blow"

        group samantha_eyes auto:
            attribute opened default

        group emma auto if_any "emma":
            attribute licking default

        group collars auto variant "licking" if_all ["emma", "licking"]
        group collars auto variant "rimming" if_all ["emma", "rimming"]

        group emma_eyes auto if_any "emma"
        group emmatongue auto variant "licking" if_all ["emma", "licking"]:
            attribute down default
        group emmatongue auto variant "rimming" if_all ["emma", "rimming"]

        group piercings auto
        group piercings auto variant "licking" if_all ["emma", "licking"]
        group piercings auto variant "rimming" if_all ["emma", "rimming"]

        group balls auto
        group balls auto variant "emma" if_all ["emma"] if_not ["emmahj"]
        group balls auto variant "emmahj" if_all ["emma", "emmahj"]

        attribute samhj null
        group dick auto if_not ["emmahj", "samhj"]
        group dick auto variant "samhj" if_not ["emmahj", "blow"]
        group dick auto variant "emmahj" if_any ["emmahj"] if_not ["samhj"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        group cumshot auto variant "samhj" if_any "cumshot" if_not ["emmahj", "blow"]
        group cumshot auto variant "emmahj" if_any "cumshot" if_not ["samhj", "blow"]

        attribute cum null
        group cum auto if_any "cum"

        group saliva

    layeredimage friendly harem cowgirl:
        attribute_function MultiPickers([DickPicker, PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker], npcs=[emma, samantha])

        attribute emma null
        attribute samantha null

        always "friendly_harem_cowgirl_bg"
        always "friendly_harem_cowgirl_bodies"

        attribute emma_pubes null
        attribute samantha_pubes null

        group multiple auto variant pregnancies

        attribute analfinger if_not "anal" if_any ["blow"]

        group emma_mouth auto
        group samantha_exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple:
            attribute emma_clit null
            attribute emma_lips null
            attribute emma_navel null
            attribute emma_pregnant_navel null
            attribute emma_nipples null
            attribute emma_tongue null
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_navel null
            attribute samantha_pregnant_navel null
            attribute samantha_tongue null

        group multiple auto variant collars

        always "friendly_harem_cowgirl_mike_balls"

        group dick auto:
            attribute outside null default
            attribute blow null
            attribute anal
            attribute vaginal

        group dick auto variant "outside" if_any "outside"

        attribute condom null
        group condom auto if_any "condom" if_not ["blow", "cum"]
        group condom auto variant "outside" if_all ["condom", "outside"] if_not ["cum"]

        attribute analfinger if_not ["anal", "blow"]

        attribute creampie null
        group creampie auto if_any "creampie" if_not "condom"

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "condom"

        attribute cum null
        group condomcum auto if_all ["condom", "cum"] if_any "outside"
        group dickcum auto if_all ["cum", "outside"] if_not ["condom"]
        group bodycum auto if_all ["cum", "outside"] if_not ["condom"]


    layeredimage friendly harem doggy:
        attribute_function MultiPickers([DickPicker, PiercingsPicker, PregnancyPicker, PubesPicker, CollarPicker], npcs=[emma, samantha])

        always "friendly_harem_doggy_bg"
        always "friendly_harem_doggy_bodies"
        attribute mike

        group multiple auto variant pregnancies

        group emma_mouth auto
        group samantha_exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple auto variant collars

        group dick auto if_any "mike"
        group dick auto variant "outside" if_not ["anal", "vaginal"] if_any "mike"

        attribute condom null
        group condom auto if_all ["condom", "mike"] if_not ["cum"]
        group condom auto variant "outside" if_all ["condom", "mike"] if_not ["anal", "vaginal", "cum"]

        attribute creampie null
        group creampie auto if_all ["creampie", "mike"] if_not "condom"

        attribute cumshot null
        group cumshot auto if_all ["cumshot", "mike"] if_not "condom"

        attribute cum null
        group condomcum auto if_all ["condom", "cum", "mike"] if_not ["anal", "vaginal"]
        group bodycum auto if_all ["cum", "mike"] if_not ["condom", "anal", "vaginal"]

        group emma_tongue auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
