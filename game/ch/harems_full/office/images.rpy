init 1:
    layeredimage office aletta foursome:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=aletta)

        group bg auto

        always:
            "office_aletta_foursome_bodies"

        group exp auto:
            attribute normal default null

        always:
            if_any "pregnant"
            "office_aletta_foursome_pregnant"

        group multiple auto variant piercings

        always:
            if_any "collar"
            "office_aletta_foursome_collar"

        group fx auto

    layeredimage office audrey foursome:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=audrey)

        group bg auto

        always:
            "office_audrey_foursome_bodies_bg"

        group exp auto:
            attribute normal default null

        always:
            if_any "pregnant"
            "office_audrey_foursome_pregnant"

        group multiple auto variant piercings

        always:
            if_any "collar"
            "office_audrey_foursome_collar"

        always:
            "office_audrey_foursome_bodies_fg"

        group fx auto

    layeredimage office lavish foursome:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=lavish)

        group bg auto

        always:
            "office_lavish_foursome_bodies"

        group exp auto:
            attribute normal default null

        always:
            if_any "pregnant"
            "office_lavish_foursome_pregnant"

        group multiple auto variant piercings

        always:
            if_any "collar"
            "office_lavish_foursome_collar"

        group fx auto

    layeredimage office shiori foursome:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PregnancyPicker], npc=shiori)

        group bg auto

        always:
            "office_shiori_foursome_bodies"

        group exp auto:
            attribute normal default null

        always:
            if_any "pregnant"
            "office_shiori_foursome_pregnant"

        group multiple auto variant piercings

        always:
            if_any "collar"
            "office_shiori_foursome_collar"

        group fx auto

    layeredimage office sixsome:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker], npcs=[audrey, lavish, shiori] )

        group bg auto

        attribute lavish

        attribute shiori

        attribute audrey

        group multiple auto variant pregnancy

        group multiple auto variant exp
        group multiple:
            attribute normal default null

        group multiple auto variant piercings

        group multiple auto variant collars

        group multiple auto variant fx

    layeredimage office threesome shiorifuck audrey:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[audrey, shiori])
        attribute aud null
        attribute anal null
        attribute vaginal null
        attribute outside null
        attribute creampie null
        attribute cum null

        always:
            "office_threesome_shiorifuck_audrey_bg"

        always:
            "office_threesome_shiorifuck_audrey_bodies_bg"

        always:
            if_any "aud"
            "office_threesome_shiorifuck_audrey_audrey_body"


        group audrey_head auto if_any "aud":
            attribute a default
        group audrey_eyes auto variant "a" if_all ["a", "aud"]:
            attribute opened default
        group audrey_eyes auto variant "b" if_all ["b", "aud"]
        group audrey_eyes auto variant "c" if_all ["c", "aud"]

        always:
            "office_threesome_shiorifuck_audrey_bodies"

        attribute shiori_pregnant
        attribute shiori_pubes
        group shiori_exp auto:
            attribute surprised default

        group outside auto if_not ["vaginal", "anal"]
        group vaginal auto if_any ["vaginal"] if_not ["outside", "anal"]
        group anal auto if_any ["anal"] if_not ["vaginal", "outside"]


        group audrey_mouth auto variant "a" if_all ["a", "aud"]
        group audrey_mouth auto variant "b" if_all ["b", "aud"]

        always:
            if_not ["suck", "anal"]
            "office_threesome_shiorifuck_audrey_mike_balls"

        group creampie auto variant "outside" if_all ["creampie", "outside"] if_not ["vaginal", "anal"]
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["outside", "anal"]
        group creampie auto variant "anal" if_all ["creampie", "anal"] if_not ["vaginal", "outside"]

        group cum auto if_any "cum"

        group multiple auto variant piercings

        always:
            if_any "aud"
            "office_threesome_shiorifuck_audrey_bodies_fg"

    layeredimage office threesome lavishfuck audrey:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[audrey, lavish])


        always:
            "office_threesome_lavishfuck_audrey_bg"


        always:
            "office_threesome_lavishfuck_audrey_bodies"


        attribute lavish_pubes


        group multiple auto variant piercings_notvaginal when not vaginal


        attribute cum null
        group cum auto if_any ["cum"]


        attribute outside null
        attribute anal null
        attribute vaginal null
        group outside auto if_not ["vaginal", "anal"]
        group outside_condom auto if_any ["condom"] if_not ["vaginal", "anal", "cum"]


        group vaginal auto if_any ["vaginal"] if_not ["outside", "anal"]


        group multiple auto variant piercings_vaginal_small when vaginal and small and not (outside or anal)
        group multiple auto variant piercings_vaginal_medium when vaginal and medium and not (outside or anal)
        group multiple auto variant piercings_vaginal_big when vaginal and hard and not (outside or anal)


        group anal auto if_any ["anal"] if_not ["vaginal", "outside", "condom"]


        group multiple auto variant piercings_spec when spec


        attribute audrey_pregnant
        attribute lavish_pregnant


        group exp_audrey auto:
            attribute audpleasure default


        group multiple auto variant piercings


        group lavish_face auto:
            attribute normal default


        group exp_lavish auto if_not "licking":
            attribute lavpleasure default


        attribute lavish_collar null
        group lavish_collar auto if_any ["lavish_collar"]
        group lavish_collar auto variant "normal" if_any ["lavish_collar"] if_not ["licking"]
        group lavish_collar auto variant "licking" if_all ["lavish_collar", "licking"]


        group multiple auto variant piercings_licking when licking
        group multiple auto variant piercings_normal when not licking


        attribute audrey_collar


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not ["condom", "vaginal", "anal"]


        attribute dickcum null
        group dickcum auto if_any "dickcum" if_not ["condom", "vaginal", "anal"]


        attribute creampie null
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["outside", "anal", "condom"]
        group creampie auto variant "anal" if_all ["creampie", "anal"] if_not ["outside", "vaginal", "condom"]


        group cum_condom auto variant "outside" if_all ["cum", "condom"]

    layeredimage office threesome shiorifuck lavish:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PubesPicker], npcs=[lavish, shiori])


        always:
            "office_threesome_shiorifuck_lavish_bg"


        always:
            "office_threesome_shiorifuck_lavish_bodies"


        attribute blush if_any ["blush"]


        group exp_shiori auto:
            attribute lookback default


        group multiple auto variant piercings_notahegao when not ahegao


        attribute shiori_pubes


        attribute lavish_collar
        attribute shiori_collar


        group fuck auto:
            attribute blowjob
            attribute anal
            attribute vaginal
            attribute outside default


        attribute condom null
        group condom auto if_any ["condom"]:
            attribute anal
            attribute vaginal
            attribute outside if_not ["cum"]


        attribute cum null
        group cum auto if_any ["cum"]:
            attribute onmouth if_any ["blowjob"]
        group cum_condom auto if_all ["cum", "condom"]:
            attribute outside


        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings_notvaginal when not vaginal


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]:
            attribute anal
            attribute vaginal


        attribute dickcum if_any "dickcum" if_not ["blowjob", "anal", "vaginal"]


        attribute cumshot if_any "cumshot" if_not ["blowjob", "anal", "vaginal"]


        group multiple auto variant piercings


        always:
            "office_threesome_shiorifuck_lavish_light"

    layeredimage office threesome lavishfuck shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[lavish, shiori])


        always:
            "office_threesome_lavishfuck_shiori_bg"


        always:
            "office_threesome_lavishfuck_shiori_bodies"


        attribute saliva


        group exp_lavish auto:
            attribute pleasure default


        attribute vaginal if_any "vaginal" if_not "outside"
        group vaginal_condom auto if_any "vaginal" if_not "outside"


        attribute outside null
        group outside auto if_any "outside" if_not "vaginal"
        group outside_condom auto if_all ["outside", "condom"] if_not ["vaginal", "cum"]


        group multiple auto variant piercings_notpreg when not pregnant


        attribute lavish_pregnant
        attribute shiori_pregnant


        attribute lavish_pubes
        attribute shiori_pubes


        group multiple auto variant piercings


        attribute dickcum null
        group dickcum auto if_all ["dickcum", "outside"]


        group cum_condom auto variant "outside" if_all ["cum", "condom", "outside"]


        attribute cumshot null
        group cumshot auto if_all ["cumshot", "outside"]


        attribute creampie null
        group creampie auto if_any "creampie":
            attribute vaginal
            attribute anal default

    layeredimage office threesome audreyfuck lavish:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[audrey, lavish])

        always:
            "office_threesome_audreyfuck_lavish_bg"

        always:
            "office_threesome_audreyfuck_lavish_bodies"


        attribute creampie


        attribute audrey_pregnant
        attribute lavish_pregnant


        attribute outside null
        group outside auto if_all ["outside"]
        group outside_condom auto if_all ["outside", "condom"]


        attribute cumshot null
        group cumshot auto if_any "cumshot" if_all ["outside", "cumshot"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"]
        group cum_condom auto variant "outside" if_all ["cum", "outside", "condom"]


        group exp_audrey auto:
            attribute pleasure default


        attribute audrey_collar
        attribute lavish_collar


        group multiple auto variant piercings_pregnant when pregnant
        group multiple auto variant piercings

    layeredimage office threesome audreyfuck shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[audrey, shiori])

        attribute cum null
        attribute creampie null
        attribute outside null
        attribute vaginal null


        always:
            "office_threesome_audreyfuck_shiori_bg"

        always:
            "office_threesome_audreyfuck_shiori_bodies"

        attribute audrey_pregnant
        attribute audrey_pubes
        attribute shiori_pregnant
        attribute shiori_pubes

        attribute shiori_collar

        group exp_audrey auto:
            attribute pleasure default
        group exp_shiori auto:
            attribute normal default

        attribute anal

        group outside auto if_not ["vaginal", "anal"]
        group outside_condom auto if_any ["condom"] if_not ["vaginal", "anal"]
        group vaginal auto if_any ["vaginal"] if_not ["outside", "anal"]
        group vaginal_condom auto if_all ["vaginal", "condom"] if_not ["outside", "anal"]
        group anal auto if_any ["anal"] if_not ["vaginal", "outside"]


        attribute creampie_anal

        group creampie auto variant "outside" if_all ["creampie", "outside"] if_not ["vaginal", "anal"]
        group creampie_condom auto variant "outside" if_all ["creampie", "outside", "condom"] if_not ["vaginal", "anal"]
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["outside", "anal", "condom"]

        group creampie auto if_all ["creampie", "anal"] if_not ["vaginal", "outside", "condom"]

        group multiple auto variant cum when cum
        attribute milk

        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings

    layeredimage office cumshare audrey lavish:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker], npcs=[audrey, lavish])

        always:
            "office_cumshare_audrey_lavish_bg"

        always:
            "office_cumshare_audrey_lavish_bodies"


        attribute audrey_collar
        attribute lavish_collar


        group multiple auto variant piercings


        attribute cum null
        group multiple auto variant cum when cum


        attribute dickcum null
        group dick auto
        group dickcum auto if_any ["dickcum"]
        group cumshot auto if_any "cumshot"

    layeredimage office cumshare audrey shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker], npcs=[audrey, shiori])
        attribute cum null
        attribute cumshot null

        always:
            "office_cumshare_audrey_shiori_bg"

        always:
            "office_cumshare_audrey_shiori_bodies"

        group multiple auto variant collars

        group fx auto
        always:
            if_not ["audreyopen"]
            "office_cumshare_audrey_shiori_exp_audreylookup"
        always:
            if_not ["shiorilookdown", "shioriopen"]
            "office_cumshare_audrey_shiori_exp_shiorilookup"
        group exp auto

        group multiple auto variant piercings_audreyopen when audreyopen
        group multiple auto variant piercings_audreynormal when not audreyopen
        group multiple auto variant piercings_shioriopen when shioriopen
        group multiple auto variant piercings_shiorinormal when not shioriopen
        group multiple auto variant piercings

        group dick auto
        group multiple auto variant cum when (cum or cumshot)
        group dickcum auto if_any ["cum", "cumshot"]
        group cumshot auto if_any "cumshot"

    layeredimage office cumshare lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[lavish, shiori])


        always:
            "office_cumshare_lavish_shiori_bg"


        always:
            "office_cumshare_lavish_shiori_mike_leg"


        always:
            "office_cumshare_lavish_shiori_bodies"


        always:
            "office_cumshare_lavish_shiori_shiori_head"
        group exp_shiori auto:
            attribute shisuck
            attribute shinormal default


        always:
            "office_cumshare_lavish_shiori_mike"


        always:
            "office_cumshare_lavish_shiori_lavish_head"
        group exp_lavish auto:
            attribute lavsuck
            attribute lavnormal default


        attribute lavish_collar
        attribute shiori_collar


        group multiple auto variant piercings


        attribute lavish_pregnant if_any "lavish_pregnant" if_not "shiori_pregnant"
        attribute shiori_pregnant if_any "shiori_pregnant" if_not "lavish_pregnant"
        attribute lavish_shiori_pregnant default if_all ["lavish_pregnant", "shiori_pregnant"]


        attribute blowjob null
        group blowjob auto if_any "blowjob" if_not "outside":
            attribute lavishbj
            attribute shioribj


        group shiori_liquid auto:
            attribute saliva if_any "saliva"
            attribute dripping if_any "dripping"


        attribute cum null
        group multiple auto variant cum when cum
        attribute lavish null
        group cum_lavish auto if_all ["cum", "lavishbj", "blowjob"]:
            attribute inmouth default
        attribute shiori null
        group cum_shiori auto if_all ["cum", "shioribj", "blowjob"]:
            attribute inmouth default


        attribute outside null
        group outside auto if_not "blowjob"


        attribute dickcum null
        group dickcum auto if_any "dickcum"


        attribute cumshot null
        group cumshot auto if_any "cumshot"


        always:
            "office_cumshare_lavish_shiori_light"

    layeredimage office ending:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, OutfitPicker], add_simple_outfit_attribute=True, append_npc_from_attributes=True)
        attribute work null
        attribute sexywork null

        always:
            "office_ending_bg"

        group multiple auto variant girl_bg
        group multiple auto variant outfit_bg
        group multiple auto variant piercings_bg

        always:
            "office_ending_couch"
        always:
            "office_ending_mike"

        group multiple auto variant girl_fg
        group multiple auto variant outfit_fg
        group multiple auto variant piercings_fg

        group collars

        always:
            if_all ["shiori_collar", "shiori"]
            "office_ending_shiori_collar_bell"
        always:
            if_any ["aletta"]
            "office_ending_aletta_glasses"

    layeredimage office foursome cumshare audrey lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[audrey, lavish, shiori])

        attribute cumshot null
        attribute dickcum null

        always:
            "office_foursome_cumshare_audrey_lavish_shiori_bg"

        always:
            "office_foursome_cumshare_audrey_lavish_shiori_bodies"

        attribute audrey_collar
        attribute audrey_pregnant
        attribute shiori_collar

        attribute cum

        group dick auto

        group dickcum auto if_any "dickcum"
        group cumshot auto if_any "cumshot" if_not "dickcum"

        group multiple auto variant piercings

    layeredimage office foursome lavishfuck audrey shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, PubesPicker], npcs=[audrey, lavish, shiori])

        attribute condom null
        attribute cum null
        attribute cumshot null
        attribute outside null
        attribute vaginal null
        attribute dickcum null

        always:
            "office_foursome_lavishfuck_audrey_shiori_bg"

        always:
            "office_foursome_lavishfuck_audrey_shiori_bodies"

        group multiple auto variant pubes
        group multiple auto variant pubes_outside when not vaginal
        group multiple auto variant pubes_vaginal when vaginal
        group multiple auto variant collars

        attribute shiori_pregnant

        group exp_lavish auto:
            attribute pleasure default

        group multiple auto variant piercings
        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings_outside when not vaginal

        group pubes auto
        group multiple auto variant pubes_vaginal when vaginal
        group multiple auto variant pubes_outside when not vaginal

        group outside auto if_not ["vaginal", "anal"]
        group condom auto if_any ["condom"] if_not ["vaginal", "anal"]

        always:
            if_any ["vaginal"]
            "office_foursome_lavishfuck_audrey_shiori_vaginal"

        always:
            if_all ["vaginal", "condom"]
            "office_foursome_lavishfuck_audrey_shiori_vaginal_condom"

        always:
            if_any ["anal"]
            "office_foursome_lavishfuck_audrey_shiori_anal"

        group hand auto:
            attribute other default

        group cum auto if_any "cum"
        group cum auto variant "vaginal" if_all ["cum", "vaginal"] if_not ["condom"]
        group cum auto variant "outside" if_all ["cum"] if_not ["vaginal", "condom", "anal"]
        group cum auto variant "outside_condom" if_all ["cum", "condom"] if_not ["vaginal", "anal"]

        group dickcum auto if_all ["dickcum"] if_not ["condom", "vaginal", "anal"]

    layeredimage office foursome shiorifuck audrey lavish:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[audrey, lavish, shiori])

        attribute cum null
        attribute outside null
        attribute vaginal null
        attribute anal null
        attribute condom null

        always:
            "office_foursome_shiorifuck_audrey_lavish_bg"

        always:
            "office_foursome_shiorifuck_audrey_lavish_bodies"

        always:
            "office_foursome_shiorifuck_audrey_lavish_fx"

        attribute audrey_collar
        attribute audrey_pregnant
        attribute lavish_collar
        attribute lavish_pregnant

        attribute asscum
        attribute cumshot

        group exp_shiori auto:
            attribute pleasure default

        group outside auto if_not ["vaginal", "anal"]
        group outside_condom auto if_any ["condom"] if_not ["vaginal", "anal"]
        group vaginal auto if_any ["vaginal"] if_not ["outside", "anal"]
        group vaginal_condom auto if_all ["vaginal", "condom"] if_not ["outside", "anal"]
        group anal auto if_any ["anal"] if_not ["vaginal", "outside"]
        group anal_condom auto if_all ["anal", "condom"] if_not ["vaginal", "outside"]

        group cum auto variant "vaginal" if_all ["cum", "vaginal"] if_not ["outside", "anal", "condom"]
        group cum auto variant "anal" if_all ["cum", "anal"] if_not ["vaginal", "outside", "condom"]

        group multiple auto variant piercings_pregnant when pregnant
        group multiple auto variant piercings

    layeredimage office foursome audreyfuck lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[audrey, lavish, shiori])

        attribute audrey null
        attribute lavish null
        attribute shiori null

        always:
            "office_foursome_audreyfuck_lavish_shiori_bg"

        attribute fx

        always:
            "office_foursome_audreyfuck_lavish_shiori_bodies"

        attribute audrey_collar
        attribute lavish_collar
        attribute shiori_collar

        attribute audrey_pregnant
        attribute lavish_pregnant
        attribute shiori_pregnant

        group exp_audrey auto:
            attribute pleasure default

        group multiple auto variant piercings
        group multiple:
            attribute audrey_ears null
            attribute lavish_clit null
            attribute lavish_navel null
            attribute lavish_pregnant_navel null
            attribute lavish_tongue null
            attribute shiori_clit null
            attribute shiori_ears null
            attribute shiori_navel null
            attribute shiori_pregnant_navel null
            attribute shiori_tongue null
        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings_pregnant when pregnant

        group dicks auto:
            attribute outside null default
            attribute vaginal null
            attribute anal null
        attribute condom null

        group outside auto if_any ["outside"]
        group outside_condom auto if_all ["condom", "outside"]
        group vaginal auto if_any ["vaginal"]
        group vaginal_condom auto if_all ["vaginal", "condom"]
        group anal auto if_any ["anal"]

        group multiple auto variant piercings_vaginal_small when vaginal and small
        group multiple auto variant piercings_vaginal_medium when vaginal and medium
        group multiple auto variant piercings_vaginal_big when vaginal and big

        attribute cum null
        attribute cumshot null
        attribute creampie null

        group cum auto variant "condom_outside" if_all ["cum", "condom"] if_not ["vaginal", "anal"]
        group cumshot auto variant "outside" if_all ["cumshot", "outside"] if_not ["vaginal", "anal"]
        group creampie auto variant "vaginal" if_all ["creampie", "vaginal"] if_not ["outside", "anal", "condom"]
        group creampie auto variant "anal" if_all ["creampie", "anal"] if_not ["outside", "vaginal", "condom"]

    layeredimage office fivesome alettafuck audrey lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, HaircutPicker], npcs=[aletta, audrey, lavish, shiori])
        attribute cum null
        attribute condom null

        always:
            "office_fivesome_alettafuck_audrey_lavish_shiori_bg"

        always:
            "office_fivesome_alettafuck_audrey_lavish_shiori_bodies"

        group multiple auto variant collars
        group multiple auto variant pregnant

        group multiple auto variant piercings
        group multiple auto variant piercings_outside when not vaginal

        attribute aletta_haircut
        group exp auto:
            attribute normal default

        group fuck auto
        group multiple auto variant piercings_vaginal when vaginal
        group outside auto if_not ["anal", "vaginal"]

        group condom auto if_any ["condom"]
        group outside_condom auto if_any ["condom"] if_not ["anal", "vaginal"]

        group creampie auto if_any "cum"
        group outside_creampie auto if_any ["cum"] if_not ["anal", "vaginal"]

        always:
            "office_fivesome_alettafuck_audrey_lavish_shiori_glasses"

    layeredimage office fivesome audreyfuck aletta lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, HaircutPicker], npcs=[aletta, audrey, lavish, shiori])
        attribute cum null
        attribute condom null

        always:
            "office_fivesome_audreyfuck_aletta_lavish_shiori_bg"

        always:
            "office_fivesome_audreyfuck_aletta_lavish_shiori_bodies"

        group multiple auto variant collars
        group multiple auto variant pregnant

        group multiple auto variant piercings

        attribute aletta_haircut
        group exp auto:
            attribute normal default

    layeredimage office fivesome lavishfuck aletta audrey shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, HaircutPicker, PubesPicker], npcs=[aletta, audrey, lavish, shiori])

        attribute aletta null
        attribute audrey null
        attribute lavish null
        attribute shiori null


        always:
            "office_fivesome_lavishfuck_aletta_audrey_shiori_bg"

        attribute insert null
        group insert_bg auto if_any "insert"
        group insert_condom auto if_all ["insert", "condom"]
        group insert_creampie auto if_all ["insert", "creampie"]


        always:
            "office_fivesome_lavishfuck_aletta_audrey_shiori_bodies"


        attribute aletta_pregnant
        attribute lavish_pregnant
        attribute shiori_pregnant


        attribute cum null
        group cum auto if_any "cum"


        group dicks auto:
            attribute flaccid null default
            attribute halfchub null
            attribute outside null
            attribute anal null
            attribute vaginal

        attribute creampie if_any ["vaginal", "anal"] if_not "outside"


        attribute cumshot null
        group cumshot auto if_all ["cumshot", "outside"] if_not ["vaginal", "anal"]


        attribute aletta_pubes
        attribute audrey_pubes null
        attribute lavish_pubes
        attribute shiori_pubes


        attribute aletta_collar
        attribute audrey_collar
        attribute lavish_collar
        attribute shiori_collar


        group multiple auto variant piercings_pregnant when pregnant
        group multiple auto variant piercings
        group multiple:
            attribute aletta_ears null
            attribute aletta_lips null
            attribute aletta_tongue null
            attribute audrey_clit null
            attribute audrey_ears null
            attribute audrey_navel null
            attribute audrey_pregnant_navel null
            attribute audrey_nipples null
            attribute audrey_nose null
            attribute audrey_tongue null
            attribute lavish_lips null
            attribute lavish_tongue null
            attribute shiori_ears null
            attribute shiori_lips null
            attribute shiori_tongue null


        attribute aletta_haircut
        attribute aletta_nohaircut

        attribute aletta_glasses null


        attribute audrey_nohaircut null
        attribute lavish_nohaircut null
        attribute shiori_nohaircut null


        group outside auto if_any "outside"


        group dicks auto:
            attribute flaccid default
            attribute halfchub
            attribute outside null
            attribute anal null
            attribute vaginal null
        attribute dickcum if_any "flaccid"


        group exp_lavish auto:
            attribute pleasure default

    layeredimage office fivesome shiorifuck aletta audrey lavish:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, DickPicker, HaircutPicker, PubesPicker], npcs=[aletta, audrey, lavish, shiori])


        always:
            "office_fivesome_shiorifuck_aletta_audrey_lavish_bg"


        always:
            "office_fivesome_shiorifuck_aletta_audrey_lavish_bodies"


        group exp_shiori auto:
            attribute pleasure default


        attribute shiori_collar
        attribute lavish_collar
        attribute audrey_collar
        attribute aletta_collar


        attribute shiori_pubes


        attribute aletta_haircut
        attribute glasses default


        attribute shiori_pregnant

        group multiple auto variant piercings

        group piercings auto variant "novaginal" if_not "vaginal"


        group dick auto
        group dick auto variant "outside" if_not ["vaginal", "anal"]

        attribute condom null
        group condom auto if_any "condom"
        group condom auto variant "outside" if_not ["anal", "vaginal"] if_any "condom"

        group piercings auto variant "vaginal" if_any "vaginal"


        attribute creampie null
        group creampie auto if_all "creampie" if_any ["vaginal", "anal"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["condom", "vaginal"," anal"]

    layeredimage office fivesome cumshare aletta audrey lavish shiori:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, HaircutPicker], npcs=[aletta, audrey, lavish, shiori])

        attribute aletta null
        attribute audrey null
        attribute lavish null
        attribute shiori null

        group dicks auto:
            attribute big null
            attribute medium null
            attribute small null



        always:
            "office_fivesome_cumshare_aletta_audrey_lavish_shiori_bg"


        always:
            "office_fivesome_cumshare_aletta_audrey_lavish_shiori_bodies"


        attribute aletta_glasses default


        attribute aletta_collar
        attribute audrey_collar
        attribute lavish_collar
        attribute shiori_collar


        attribute aletta_haircut
        attribute aletta_nohaircut
        attribute audrey_nohaircut null
        attribute lavish_nohaircut null
        attribute shiori_nohaircut null


        group multiple auto variant piercings
        group multiple:
            attribute aletta_clit null
            attribute aletta_ears null
            attribute aletta_navel null
            attribute aletta_pregnant_navel null
            attribute aletta_nipples null
            attribute audrey_clit null
            attribute audrey_ears null
            attribute audrey_navel null
            attribute audrey_pregnant_navel null
            attribute audrey_nipples null
            attribute lavish_clit null
            attribute lavish_navel null
            attribute lavish_nipples null
            attribute shiori_clit null
            attribute shiori_ears null
            attribute shiori_navel null
            attribute shiori_pregnant_navel null
            attribute shiori_nipples null



        attribute dick null
        group dick auto if_any ["dick"]


        attribute fx null
        group fx auto if_any ["fx"]






        attribute cum_face_onaletta
        attribute cum_face_onaudrey
        attribute cum_face_onlavish
        attribute cum_face_onshiori
        attribute cum_mouth_onaletta
        attribute cum_mouth_onaudrey
        attribute cum_mouth_onlavish
        attribute cum_mouth_onshiori


        attribute cumshot null
        group cumshot auto if_any ["cumshot"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
