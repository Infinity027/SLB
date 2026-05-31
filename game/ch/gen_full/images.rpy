init 1:
    layeredimage nightclub foursome aletta lexi:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker], npcs=[aletta, lexi])
        attribute naked null
        attribute cum null
        always:
            "nightclub_foursome_aletta_lexi_bg"
        group multiple auto variant body
        attribute lexi_pregnant
        attribute aletta_pregnant
        group alettaexp auto:
            attribute alettalewd default
        group lexiexp auto:
            attribute lexilewd default
        group multiple auto variant piercings
        group lexioutfit auto if_not ["naked"]
        group alettaoutfit auto if_not ["naked"]
        group alettaoutfit auto variant "pregnant" if_any "aletta_pregnant" if_not ["naked"]

        attribute aletta_collar
        group dick auto:
            attribute medium null
        always:
            if_any ["cum"]
            "nightclub_foursome_aletta_lexi_cum"

    layeredimage nightclub cumshare aletta lexi:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker], npcs=[aletta, lexi])
        attribute naked null
        attribute cum null
        always:
            "nightclub_cumshare_aletta_lexi_bg"
        always:
            "nightclub_cumshare_aletta_lexi_body_lexi"
        attribute lexi_pregnant
        attribute lexi_collar
        group multiple auto variant lexipiercings
        attribute lexi_date if_not ["naked"]
        group lexiexp auto:
            attribute lexilewd default

        always:
            "nightclub_cumshare_aletta_lexi_body_aletta"

        attribute aletta_collar
        group multiple auto variant alettapiercings
        attribute aletta_date if_not ["naked"]
        group alettaexp auto:
            attribute alettalewd default

        always:
            "nightclub_cumshare_aletta_lexi_men"
        group dick auto
        group cum auto if_any "cum"
        attribute cum_dwayne

    layeredimage nightclub bj aletta lexi:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker], npcs=[aletta, lexi])
        attribute naked null
        attribute cum null
        always:
            "nightclub_bj_aletta_lexi_bg"
        group multiple auto variant body
        attribute lexi_pregnant
        attribute aletta_pregnant
        group alettaexp auto:
            attribute alettanormal default
        group lexiexp auto:
            attribute lexinormal default
        group multiple auto variant piercings
        group outfit auto if_not ["naked"]

        attribute lexi_collar
        always:
            "nightclub_bj_aletta_lexi_mike_balls"
        group dick auto
        group cum auto if_any "cum"
        always:
            if_any ["cum"]
            "nightclub_bj_aletta_lexi_cum_dwayne"

    layeredimage workingwith:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, OutfitPicker, RoomPicker, HaircutPicker], add_simple_pregnant_attribute=True, add_simple_outfit_attribute=True, append_npc_from_attributes=True)

        attribute naked null

        group bg auto

        always:
            "workingwith_body_mike"
        always:
            "workingwith_outfits_mike_work"

        group girls auto
        group girls auto variant "haircut" if_any ["aletta_haircut"]
        group girls auto variant "nohaircut" if_any ["aletta_nohaircut"]

        group pregnancy auto if_any "pregnant"

        group multiple auto variant piercings
        group multiple auto variant piercings_hidden when naked

        group outfits auto if_not ["naked"]
        group pregnancy auto if_all "pregnant" if_any ["aletta_sexywork", "lavish_sexywork"]
        group outfits_pregnant auto if_any "pregnant" if_not ["naked"]

        group collars auto

        group hairs auto

        group glasses auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
