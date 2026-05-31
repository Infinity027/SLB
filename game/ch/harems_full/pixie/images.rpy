init python:
    class PixieEndingPicker(object):
        def __call__(self, attr):
            attr.add("mike")
            attr.add("morgan")
            attr.add("kleio")
            
            if morgan.flags.mikeBabies >= 1:
                attr.add('boy')
            
            if kleio.flags.mikeBabies >= 1:
                attr.add('girl')
            if enable_debug_picker:
                renpy.log(f"PixieEndingPicker results: {attr}")
            return attr

init 1:
    layeredimage kleio morgan threesome:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker], npcs=[kleio, morgan])
        attribute cumshot null

        always:
            "kleio_morgan_threesome_bg"
        always:
            "kleio_morgan_threesome_body"

        group exp auto:
            attribute open default

        group morganexp auto:
            attribute morganopen default

        attribute morgan_makeup null
        group makeup auto if_any "morgan_makeup"

        group multiple auto variant pregnancy

        group haircuts auto

        group multiple auto variant piercings

        attribute morgan_collar

        group fuck auto:
            attribute out default

        group cumshot auto:
            if_any "cumshot"

        group multiple auto variant fx

    layeredimage kleio morgan cumshot:
        attribute_function MultiPickers([PiercingsPicker, CollarPicker, HaircutPicker, MCCGPicker], npcs=[kleio, morgan])


        attribute cum null
        attribute dickcum null
        attribute facecum null
        attribute kleio_clit null
        attribute kleio_navel null
        attribute kleio_nohaircut null
        attribute kleio_tongue null
        attribute morgan_clit null
        attribute morgan_makeup null
        attribute morgan_navel null
        attribute morgan_tongue null


        always "kleio_morgan_cumshot_bg"


        attribute kleio
        attribute morgan
        attribute mikemc


        group dick auto
        group dickcum auto when dickcum
        attribute mc_pubes


        group heads auto:
            attribute look default
        group makeup auto when morgan_makeup


        group collars auto variant look when look
        group collars auto variant kiss when kiss


        group hair auto variant look when look
        group hair auto variant kiss when kiss


        attribute saliva when kiss
        attribute mouthcum when kiss
        group facecum auto when facecum
        group cum auto when cum


        group multiple auto variant piercings
        group multiple auto variant piercings_look when look
        group multiple auto variant piercings_kiss when kiss


        always "kleio_morgan_cumshot_hands"
        attribute wiggle




    layeredimage pixie morgan cunnilingus:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npcs=[kleio, morgan])

        always:
            "pixie_morgan_cunnilingus_bg"

        attribute morgan

        attribute kleio
        group kleio_tattoos:
            attribute kleio_angel null
            attribute kleio_wolf null

        group multiple auto variant pubes

        group multiple auto variant pregnancy

        attribute mike

        group multiple auto variant collars

        group multiple auto variant hairs
        group multiple:
            attribute morgan_nohaircut null

        group multiple auto variant piercings
        group multiple:
            attribute kleio_ears null

        attribute morgan_makeup

    layeredimage pixie threesome kleiofuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, HaircutPicker], npcs=[kleio, morgan])

        always:
            "pixie_threesome_kleiofuck_bg"

        attribute kleio

        attribute kleio_pregnant
        attribute kleio_collar

        group multiple auto variant piercings

        attribute morgan

        attribute morgan_pregnant
        attribute morgan_collar

        always:
            "pixie_threesome_kleiofuck_mike"

        attribute morgan_makeup

        group multiple auto variant hairs

        always:
            "pixie_threesome_kleiofuck_bodies_fg"

        attribute out null
        group dick auto if_any "out"

        attribute cum null
        group cumshot auto if_any "cum"

        always:
            "pixie_threesome_kleiofuck_fg"

    layeredimage pixie kleio cunnilingus:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npcs=[kleio, morgan])

        always:
            "pixie_kleio_cunnilingus_bg"

        attribute kleio

        group multiple auto variant pubes

        group multiple auto variant pregnancy

        always:
            "pixie_kleio_cunnilingus_mike"

        attribute morgan

        group multiple auto variant collars

        group multiple auto variant hairs

        group multiple auto variant piercings

        attribute morgan_makeup

        always:
            "pixie_kleio_cunnilingus_fg"

    layeredimage pixie cumshare:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, PubesPicker, DickPicker], npcs=[kleio, morgan])

        always:
            "pixie_cumshare_bg"

        always:
            "pixie_cumshare_mikeleg"

        attribute kleio

        attribute kleio_clit

        attribute kleio_pregnant

        attribute kleio_ears

        group kleio_hairs auto

        attribute morgan

        group multiple auto variant pubes

        group multiple auto variant piercings

        attribute morgan_pregnant

        group multiple auto variant collars

        group multiple auto variant morgan_hairs

        attribute morgan_makeup

        always:
            "pixie_cumshare_mike"

        always:
            "pixie_cumshare_mikethumb"

        group dick auto

        always:
            "pixie_cumshare_mikearm"

        attribute cum null
        group cumshot auto if_any "cum"

    layeredimage pixie handjob:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, DickPicker, PiercingsPicker, PregnancyPicker, PubesPicker], npcs=[kleio, morgan])

        always:
            "pixie_handjob_bg"

        always:
            "pixie_handjob_mike"

        attribute kleio

        group multiple auto variant pubes

        group dick auto

        always:
            "pixie_handjob_kleio_fingers"

        attribute morgan

        group multiple auto variant collars

        group multiple auto variant hairs

        group multiple auto variant pregnancy

        group multiple auto variant piercings

        attribute morgan_makeup

        always:
            "pixie_handjob_mike_hands"

    layeredimage pixie threesome morganfuck:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker, HaircutPicker], npcs=[kleio, morgan])

        always:
            "pixie_threesome_morganfuck_bg"

        attribute kleio
        group kleio_tattoos:
            attribute kleio_angel null
            attribute kleio_wolf null

        always:
            "pixie_threesome_morganfuck_mike"

        attribute morgan

        group multiple auto variant pubes

        group multiple auto variant collars

        group multiple auto variant pregnancy

        attribute drool

        group multiple auto variant piercings
        group multiple:
            attribute kleio_ears null

        attribute morgan_makeup

        group multiple auto variant hairs
        group multiple:
            attribute morgan_nohaircut null

        group piercings auto variant "out" if_not "vaginal"

        attribute vaginal null
        attribute anal null
        attribute out null

        group dick auto variant "vaginal" if_any "vaginal" if_not ["anal"]
        group dick auto variant "anal" if_any "anal" if_not ["vaginal"]
        group dick auto variant "outside" if_not ["anal", "vaginal"]

        attribute cum null
        group cumshot auto if_any "cum" if_not ["anal", "vaginal"]

        group piercings auto variant "vaginal" if_any "vaginal"

        always:
            "pixie_threesome_morganfuck_fg"

    layeredimage pixie blowjob:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, DickPicker, PiercingsPicker, PregnancyPicker], npcs=[kleio, morgan])

        always:
            "pixie_blowjob_bg"

        always:
            "pixie_blowjob_mike_leg"

        attribute kleio

        attribute kleio_pregnant null
        always:
            if_any "kleio_pregnant"
            "pixie_blowjob_pregnancy_kleio_pregnant"

        group tattoos auto

        always:
            "pixie_blowjob_mike"

        attribute morgan

        attribute morgan_pregnant null
        always:
            if_any "morgan_pregnant"
            "pixie_blowjob_pregnancy_morgan_pregnant"

        group multiple auto variant collars

        group multiple auto variant hairs

        group multiple auto variant piercings

        attribute morgan_makeup

        always:
            "pixie_blowjob_mike_arm"

        group dick auto

        attribute drool null
        always:
            "pixie_blowjob_drool"

    layeredimage pixie ending:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, PiercingsPicker, PregnancyPicker, OutfitPicker, PixieEndingPicker], npcs=[kleio, morgan], add_simple_outfit_attribute=True)
        attribute swimsuit default null
        always:
            "pixie_ending_bg"

        group multiple auto variant footprints
        group multiple auto variant castshadows

        attribute boy
        attribute girl

        always:
            "pixie_ending_mike"

        attribute kleio

        attribute morgan

        attribute morgan_makeup

        group multiple auto variant hairs

        group multiple auto variant pregnancy

        group multiple auto variant collars

        group multiple auto variant piercings

        group botkleio auto

        group botmorgan auto

        group multiple auto variant top

        group multiple auto variant shadows
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
