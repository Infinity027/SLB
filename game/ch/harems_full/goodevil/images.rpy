init 1:
    layeredimage goodevil bj:
        attribute_function MultiPickers([OutfitPicker, PiercingsPicker, CollarPicker, MCPicker], npcs=[harmony, lexi], add_simple_outfit_attribute=True)

        attribute mikemc null

        group bg auto:
            attribute beach default

        always "goodevil_bj_bodies"

        attribute naked null
        group multiple auto variant bot when not naked
        group multiple auto variant top when not naked
        group mc_outfits auto if_not "naked":
            attribute swimsuit null default

        group multiple auto variant collars

        group heads auto:
            attribute normal default

        group multiple auto variant piercings_normal when normal or suck
        group multiple auto variant piercings_lick when lick
        group multiple auto variant piercings_facial when facial

        attribute saliva if_any "lick"

        always "goodevil_bj_mc_balls"
        attribute cumshare

        group dick_location:
            attribute middle default null
            attribute left null
            attribute right null

        group dick auto variant "mc_big" if_any "mc_big" if_not "suck"
        group dick auto variant "mc_medium" if_any "mc_medium" if_not "suck"
        group dick auto variant "mc_small" if_any "mc_small" if_not "suck"

        group suckdick auto variant "mc_big" if_all ["mc_big", "suck"]
        group suckdick auto variant "mc_medium" if_all ["mc_medium", "suck"]
        group suckdick auto variant "mc_small" if_all ["mc_small", "suck"]
        group suck auto variant "mc_big" if_all ["mc_big", "suck"]
        group suck auto variant "mc_medium" if_all ["mc_medium", "suck"]
        group suck auto variant "mc_small" if_all ["mc_small", "suck"]

        attribute cum null
        attribute cumshot null
        attribute facial null
        attribute inmouth null

        group cum auto if_any "cum"

        group cumshot auto variant "mc_big" if_all ["mc_big", "cumshot"]
        group cumshot auto variant "mc_medium" if_all ["mc_medium", "cumshot"]
        group cumshot auto variant "mc_small" if_all ["mc_small", "cumshot"]

        group cum auto variant "facial" if_all ["cum", "facial"]

        group cum_inmouth auto variant "mc_big" if_all ["cum", "inmouth", "mc_big"]
        group cum_inmouth auto variant "mc_medium" if_all ["cum", "inmouth", "mc_medium"]
        group cum_inmouth auto variant "mc_small" if_all ["cum", "inmouth", "mc_small"]


    layeredimage goodevil threesome harmonyfuck:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, MCCGPicker], npcs=[harmony, lexi])
        attribute mikemc null
        group mcoutfits:
            attribute mc_casual null
            attribute mc_date null

        group bg auto:
            attribute trailer default

        always:
            "goodevil_threesome_harmonyfuck_bodies"

        group multiple auto variant collars

        group multiple auto variant pregnancies

        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "small" if_any "mc_small"
        group dick auto variant "medium" if_any "mc_medium"
        group dick auto variant "big" if_any "mc_big"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie":
            attribute harmony_navel null
            attribute harmony_nipples null
            attribute lexi_clit null

        group multiple auto variant piercings


    layeredimage goodevil threesome lexifuck:
        attribute_function MultiPickers([DickPicker, PiercingsPicker, CollarPicker, PregnancyPicker], npcs=[harmony, lexi])


        group bg auto:
            attribute trailer default


        always:
            "goodevil_threesome_lexifuck_bodies"


        group multiple auto variant collars


        group multiple auto variant piercings
        group multiple:
            attribute harmony_ears null
            attribute harmony_nose null
            attribute harmony_tongue null
            attribute lexi_navel null
            attribute lexi_tongue null


        group multiple auto variant pregnancies


        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick auto variant "out" if_any ["out"]
        group dick auto variant "vaginal" if_any ["vaginal"]
        group dick auto variant "anal" if_any ["anal"]

        attribute cum null
        group cum auto if_all ["cum", "out"]
        group cum auto variant "vaginal" if_all ["vaginal","cum"]
        group cum auto variant "anal" if_all ["anal","cum"]


    layeredimage goodevil threesome cumshare:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, PregnancyPicker, MCCGPicker], npcs=[harmony, lexi])
        attribute mikemc null
        group mcoutfits:
            attribute mc_casual null
            attribute mc_date null

        group bg auto:
            attribute trailer default

        always:
            "goodevil_threesome_cumshare_bodies"

        group multiple auto variant collars
        group multiple auto variant pregnancies
        group multiple auto variant piercings
        group multiple:
            attribute lexi_navel null
            attribute lexi_tongue null
            attribute lexi_nipples null

        group dick_position:
            attribute out null default
            attribute vaginal null

        group dick auto

        attribute cumshot null
        group cumshot auto if_any "cumshot"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
