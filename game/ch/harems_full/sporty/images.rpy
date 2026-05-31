init 1:
    layeredimage sporty blowjob:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PiercingsPicker, DickPicker], npcs=[ayesha, hanna])

        group bg auto:
            attribute bedroom default

        always:
            "sporty_blowjob_bodies"

        group multiple auto variant pregnancy

        attribute sweat

        group multiple auto variant piercings
        group multiple auto variant collars

        always:
            if_not "hannabj"
            "sporty_blowjob_mouth_hannaopenmouth"

        group cum auto

        attribute hannablush

        group hannaeyes auto:
            attribute hannaopeneyes default

        group ayeshaeyes auto:
            attribute ayeshaopeneyes default

        group bjdick auto if_any ["ayeshabj", "hannabj"]
        group dick auto if_not ["ayeshabj", "hannabj"]

        group multiple auto variant fingers
        group multiple auto variant squirts

        attribute cum null
        group cum auto if_any "cum"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute dickcum null
        group dickcum auto if_any "dickcum"

        always:
            if_any "dickcum"
            "sporty_blowjob_hannainmouth"

    layeredimage sporty harem ending:
        attribute_function MultiPickers([EndingKidPicker], npcs=[ayesha, hanna])

        always "sporty_harem_ending_bg"


        group multiple auto variant kids
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
