init 1:
    layeredimage metal harem doggy:
        attribute_function MultiPickers([MCCGPicker, HaircutPicker, PiercingsPicker, PubesPicker], npcs=[sasha, scottie])

        attribute sasha null
        attribute nosasha null
        attribute scottie null
        attribute noscottie null

        group bg auto:
            attribute bedroom4 default

        group shadow auto when (sashafront and not nosasha) or (scottiefront and not noscottie)
        group reflection auto when bedroom4 and (sashaback and not nosasha) or (scottieback and not noscottie)


        group position_front auto:
            attribute sashafront null
            attribute scottiefront null default

        group position_back auto:
            attribute sashaback null default
            attribute scottieback null

        group sasha_mouth auto:
            attribute sashahappy null default
            attribute sashaahegao null

        group sasha_eyes auto:
            attribute sashaopen null default
            attribute sashapleasure null

        group scottie_mouth auto:
            attribute scottiehappy null default
            attribute scottieahegao null

        group scottie_eyes auto:
            attribute scottieopen null default
            attribute scottiepleasure null

        group strapon auto:
            attribute strapvaginal null default
            attribute strapanal null



        group scottie_position auto when scottiefront and not noscottie

        attribute blush when scottiefront and not noscottie

        group scottiemouth auto variant front when scottiefront and not noscottie
        group scottieeyes auto variant front when scottiefront and not noscottie

        group dicks auto variant front when scottiefront and not noscottie:
            attribute out default

        attribute creampie when scottiefront and not noscottie
        attribute cumshot null
        group cumshot auto when scottiefront and not noscottie and cumshot

        attribute scottie_pubes null


        group sasha_position auto when sashafront and not nosasha

        group boobjobs auto variant front when sashafront and not nosasha
        group haircuts auto variant front when sashafront and not nosasha

        group sashamouth auto variant front when sashafront and not nosasha
        group sashaeyes auto variant front when sashafront and not nosasha

        group multiple auto variant piercings_front when sashafront and not nosasha
        group piercings_boobjob auto variant front when sashafront and sasha_boobjob and not nosasha
        group piercings_noboobjob auto variant front when sashafront and sasha_noboobjob and not nosasha

        group multiple:
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null

        attribute sasha_pubes when sashafront and not nosasha

        attribute sashasquirt when sashafront and not nosasha


        attribute breemc
        group mc_mouth auto
        group mc_eyes auto:
            attribute breeopen default

        attribute mc_haircut
        attribute mc_nohaircut null
        attribute mc_pregnant
        attribute mc_pubes
        attribute mc_collar null

        group multiple auto variant mc_piercings:
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        attribute vibrator null
        group vibrator auto when vibrator:
            attribute off default

        attribute mc_casual null



        group sasha_position auto when not nosasha:
            attribute sashafront null
            attribute sashaback

        group boobjobs auto variant back when sashaback and not nosasha

        attribute sasha_noboobjob null

        attribute sasha_pubes null

        group haircuts auto variant back when sashaback and not nosasha

        group sashamouth auto variant back when sashaback and not nosasha
        group sashaeyes auto variant back when sashaback and not nosasha

        group multiple auto variant piercings_back when sashaback and not nosasha
        group piercings_boobjob auto variant back when sashaback and sasha_boobjob and not nosasha
        group piercings_noboobjob auto variant back when sashaback and sasha_noboobjob and not nosasha

        group hands auto when sashaback and not nosasha:
            attribute slap default

        group strapon auto when sashaback and not nosasha



        group scottie_position auto when scottieback and not noscottie

        attribute scottie_nohaircut null
        group cumshot auto when scottieback and not noscottie and cumshot

        attribute vibrator
        attribute dildo

        always "metal_harem_doggy_arm_front" when scottiefront and not noscottie

    layeredimage metal harem reverse cowgirl:
        attribute_function MultiPickers([MCCGPicker, HaircutPicker, PiercingsPicker], npcs=[sasha])

        group bg auto:
            attribute bedroom3 default

        always "metal_harem_reverse_cowgirl_bodies"

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute sasha_nohaircut
        attribute sasha_haircut null

        attribute cum
        attribute squirt

        always "metal_harem_reverse_cowgirl_exp_scottie"

        group sasha_eyes auto:
            attribute sashaopen default
        group sasha_mouth auto:
            attribute sashahappy default

        group mc_eyes auto:
            attribute breeopen default
        group mc_mouth auto:
            attribute breehappy default

        attribute blindfold
        attribute mc_pregnant
        attribute mc_pubes
        attribute sasha_pregnant

        group multiple auto variant mc_piercings:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        group multiple auto variant sasha_piercings:
            attribute sasha_clit null
            attribute sasha_lips null
            attribute sasha_nipples null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_tongue null

        attribute sasha_noboobjob null
        attribute sasha_boobjob

        attribute mc_collar

    layeredimage metal harem missionary:
        attribute_function MultiPickers([MCCGPicker, HaircutPicker, PiercingsPicker, CollarPicker, PubesPicker], append_npc_from_attributes=True)

        attribute mc_casual null

        group bg auto:
            attribute bedroom4 default

        always "metal_harem_missionary_sasha_leg" when sasha

        attribute breemc
        attribute mc_nohaircut null
        attribute mc_haircut
        attribute mc_pubes
        attribute mc_pregnant

        group multiple auto variant mc_piercings:
            attribute mc_ears null
            attribute mc_lips null

        group eyes auto when not (sasha):
            attribute breewide default

        group mouth auto:
            attribute breeopen default

        attribute sasha
        attribute sasha_pubes

        group sasha_arms auto when sasha:
            attribute boob default

        attribute sasha_noboobjob null
        attribute sasha_boobjob

        attribute sasha_nohaircut
        attribute sasha_haircut null

        group multiple auto variant sasha_piercings when sasha:
            attribute sasha_lips null
            attribute sasha_pregnant_navel null
            attribute sasha_tongue null
        group sasha_piercings_boobjob auto when sasha and sasha_boobjob
        group sasha_piercings_noboobjob auto when sasha and sasha_noboobjob
        group sasha_eyes auto when sasha:
            attribute sashaopen default
        group sasha_mouth auto when sasha:
            attribute sashahappy default

        always "metal_harem_missionary_mc_leg"

        attribute scottie null
        attribute scottie_nohaircut null
        group dick auto when scottie:
            attribute out default

        attribute creampie null
        group creampie auto when creampie

        attribute cumshot when out

        attribute cum null
        group cum auto when cum

        group scottie auto when scottie:
            attribute far default

        group scottie_exp auto when scottie and far:
            attribute scottiehappy default

        attribute scottie_pubes null

        attribute mc_collar
        attribute leash

        group fg auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
