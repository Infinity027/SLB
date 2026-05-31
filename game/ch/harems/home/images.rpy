init 1:
    layeredimage bitches:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PiercingsPicker], npcs=[bree, sasha])
        attribute bree null
        attribute sasha null

        group arms auto:
            attribute nohold null default
            attribute hold null


        always:
            "bitches_bg"


        group bj auto:
            attribute breebj null
            attribute sashabj null


        group mike auto if_not ["breebj", "sashabj"]:
            attribute walk default
            attribute stand

        group mike auto variant "breebj" if_any ["breebj"]
        group mike auto variant "sashabj" if_any ["sashabj"]


        group breearm auto variant "nohold" if_any ["nohold", "sashabj"]
        group sashaarm auto variant "nohold" if_any ["nohold", "breebj"]


        group position auto variant "bree":
            attribute walk
            attribute stand


        group position auto variant "sasha":
            attribute walk
            attribute stand


        attribute breepee if_any ["stand"]
        attribute sashapee if_any ["stand"]


        group multiple auto variant pubic_walk when walk
        group multiple auto variant pubic_stand when stand


        attribute bree_nohaircut null
        group haircuts auto variant "walk" if_any ["walk"]
        group haircuts auto variant "stand" if_any ["stand"]


        group multiple auto variant piercings_behind_walk when walk


        group multiple auto variant pregnancy_walk when walk
        group multiple auto variant pregnancy_stand when stand


        attribute sasha_noboobjob null
        group bb auto variant "walk" if_any ["walk"]



        group exp_bree auto variant "walk" if_any ["walk"]:
            attribute breenormal default
            attribute breehappy
        group exp_sasha auto variant "walk" if_any ["walk"]:
            attribute sashanormal default
            attribute sashahappy

        group eyes_bree auto if_any ["stand"]:
            attribute breeopeneyes default
            attribute breecloseeyes
        group eyes_sasha auto if_any ["stand"]:
            attribute sashaopeneyes default
            attribute sashacloseeyes

        group mouth_bree auto if_any ["stand"] if_not ["inside"]:
            attribute breetongueout default
            attribute breeswallow
        group mouth_sasha auto if_any ["stand"] if_not ["inside"]:
            attribute sashatongueout default
            attribute sashaswallow

        group mouth_bree auto if_all ["stand", "inside", "sashabj"]
        group mouth_sasha auto if_all ["stand", "inside", "breebj"]


        group piercings multiple:
            attribute bree_ears null
        group multiple auto variant piercings_walk when walk
        group multiple auto variant piercings_stand when stand
        group multiple auto variant piercings_walk_notbb when walk and not sasha_boobjob
        group multiple auto variant piercings_walk_bb when walk and sasha_boobjob


        group multiple auto variant collars_walk when walk
        group multiple auto variant collars_stand when stand


        attribute cum null
        group multiple auto variant cum when cum 


        attribute leash default null
        group breeleash auto if_all ["bree_collar", "leash"] if_not ["breebj"]:
            attribute walk
            attribute stand
        group sashaleash auto if_all ["sasha_collar", "leash"] if_not ["sashabj"]:
            attribute walk
            attribute stand
        group breeleash auto variant "breebj" if_all ["breebj", "bree_collar", "leash"]


        group mikedick auto:
            attribute inside null
            attribute outside null default
        group dick_inside auto variant "breebj" if_all ["inside", "breebj"]
        group dick_inside auto variant "sashabj" if_all ["inside", "sashabj"]
        group dick_outside auto variant "breebj" if_all ["outside", "breebj"]
        group dick_outside auto variant "sashabj" if_all ["outside", "sashabj"]


        attribute dickcum null
        group dickcum_outside auto variant "breebj" if_all ["dickcum", "outside", "breebj"]
        group dickcum_outside auto variant "sashabj" if_all ["dickcum", "outside", "sashabj"]


        attribute cumshot null
        group cumshot_inside auto variant "breebj" if_all ["cumshot", "inside", "breebj"]
        group cumshot_inside auto variant "sashabj" if_all ["cumshot", "inside", "sashabj"]
        group cumshot_outside auto variant "breebj" if_all ["cumshot", "outside", "breebj"]
        group cumshot_outside auto variant "sashabj" if_all ["cumshot", "outside", "sashabj"]


        group breearm auto variant "hold_breebj" if_all ["hold", "breebj"]
        group sashaarm auto variant "hold_sashabj" if_all ["hold", "sashabj"]


        group bb auto variant "stand" if_any ["stand"]
        group multiple auto variant piercings_stand_notbb when stand and not sasha_boobjob
        group multiple auto variant piercings_stand_bb when stand and sasha_boobjob
        group sashaleash auto variant "sashabj" if_all ["sashabj", "sasha_collar", "leash"]


        always:
            "bitches_light"

    layeredimage bj breeleximinamisamsasha:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker, DickPicker], npcs=[bree, "lexi", minami, samantha, sasha])
        attribute mike
        always:
            "bj_breeleximinamisamsasha_bg"
        always:
            if_any ["mike", "breeblow", "breelick", "lexiblow", "lexilick", "minamiblow", "minamilick", "samanthablow", "samanthalick", "sashablow", "sashalick"]
            "bj_breeleximinamisamsasha_mike"


        group sashaloc auto:
            attribute sashaback default


        group sashaback_exp auto:
            if_any "sashaback"
            if_not ["sashablow", "sashalick"]
            attribute sashanormal default
        always:
            if_any "sashainmouth"
            if_not "sashafront"
            "bj_breeleximinamisamsasha_sashaback_exp_sashaopenmouth"

        group pregnancies auto variant "sashaback" if_any "sashaback"
        group collars auto variant "sashaback" if_any "sashaback"
        group boobjob auto variant "sashaback" if_any "sashaback"
        group haircuts auto variant "sashaback" if_any "sashaback"
        group multiple auto variant piercings_sashaback when sashaback
        group multiple auto variant piercings_sashaback_boobjob when sashaback and sasha_boobjob
        group multiple auto variant piercings_sashaback_noboobjob when sashaback and not sasha_boobjob



        group sashafront_exp auto:
            if_any "sashafront"
            attribute sashanormal default
        group pregnancies auto variant "sashafront" if_any "sashafront"
        group collars auto variant "sashafront" if_any "sashafront"
        group boobjob auto variant "sashafront" if_any "sashafront"
        group haircuts auto variant "sashafront" if_any "sashafront"
        group multiple auto variant piercings_sashafront when sashafront
        group multiple auto variant piercings_sashafront_boobjob when sashafront and sasha_boobjob
        group multiple auto variant piercings_sashafront_noboobjob when sashafront and not sasha_boobjob


        group samanthaloc auto:
            attribute samanthaback default


        group samanthaback_exp auto:
            if_not "samanthainmouth"
            if_any "samanthaback"
            attribute samanthanormal default
        always:
            if_any "samanthainmouth"
            if_not "samanthafront"
            "bj_breeleximinamisamsasha_samanthaback_exp_samanthaopenmouth"
        group pregnancies auto variant "samanthaback" if_any "samanthaback"
        group collars auto variant "samanthaback" if_any "samanthaback"
        group multiple auto variant piercings_samanthaback when samanthaback


        group pregnancies auto variant "samanthafront" if_any "samanthafront"
        group collars auto variant "samanthafront" if_any "samanthafront"
        group multiple auto variant piercings_samanthafront when samanthafront


        group breeloc auto:
            attribute breeback default


        group breeback_exp auto:
            if_any "breeback"
            if_not "breeinmouth"
            attribute breenormal default
        always:
            if_any "breeinmouth"
            if_not "breefront"
            "bj_breeleximinamisamsasha_breeback_exp_breeopenmouth"

        group pregnancies auto variant "breeback" if_any "breeback"
        group collars auto variant "breeback" if_any "breeback"
        group multiple auto variant piercings_breeback when breeback


        group pregnancies auto variant "breefront" if_any "breefront"
        group collars auto variant "breefront" if_any "breefront"
        group multiple auto variant piercings_breefront when breefront


        group minamiloc auto:
            attribute minamiback default


        group collars auto variant "minamiback" if_any "minamiback"
        group haircuts auto variant "minamiback" if_any "minamiback"

        group minamiback_exp auto:
            if_any "minamiback"
            if_not "minamiinmouth"
            attribute minaminormal default
        always:
            if_any "minamiinmouth"
            if_not "minamifront"
            "bj_breeleximinamisamsasha_minamiback_exp_minamiopenmouth"
        group pregnancies auto variant "minamiback" if_any "minamiback"
        group multiple auto variant piercings_minamiback when minamiback


        group collars auto variant "minamifront" if_any "minamifront"
        group haircuts auto variant "minamifront" if_any "minamifront"
        group pregnancies auto variant "minamifront" if_any "minamifront"
        group multiple auto variant piercings_minamifront when minamifront


        group lexiloc auto:
            attribute lexiback default


        group lexiback_exp auto:
            if_any "lexiback"
            if_not "lexiinmouth"
            attribute lexinormal default
        always:
            if_any "lexiinmouth"
            if_not "lexifront"
            "bj_breeleximinamisamsasha_lexiback_exp_lexiopenmouth"

        group pregnancies auto variant "lexiback" if_any "lexiback"
        group collars auto variant "lexiback" if_any "lexiback"
        group multiple auto variant piercings_lexiback when lexiback



        group pregnancies auto variant "lexifront" if_any "lexifront"
        group collars auto variant "lexifront" if_any "lexifront"
        group multiple auto variant piercings_lexifront when lexifront

        group dick auto:
            if_any ["mike"]
            if_not ["breeblow", "breelick", "lexiblow", "lexilick", "minamiblow", "minamilick", "samanthablow", "samanthalick", "sashablow", "sashalick"]

        group action auto:
            if_any ["breefront", "lexifront", "minamifront", "samanthafront", "sashafront"]

        group cumbackbree auto:
            if_any ["breeback"]
            if_not ["breefront"]

        group cumfrontbree auto:
            if_any ["breefront"]
            if_not ["breeback"]

        group cumbacklexi auto:
            if_any ["lexiback"]
            if_not ["lexifront"]

        group cumfrontlexi auto:
            if_any ["lexifront"]
            if_not ["lexiback"]

        group cumbackminami auto:
            if_any ["minamiback"]
            if_not ["minamifront"]

        group cumfrontminami auto:
            if_any ["minamifront"]
            if_not ["minamiback"]

        group cumbacksamantha auto:
            if_any ["samanthaback"]
            if_not ["samanthafront"]

        group cumfrontsamantha auto:
            if_any ["samanthafront"]
            if_not ["samanthaback"]

        group cumbacksasha auto:
            if_any ["sashaback"]
            if_not ["sashafront"]

        group cumfrontsasha auto:
            if_any ["sashafront"]
            if_not ["sashaback"]

        group mikecum auto

    layeredimage bj breeminamisamsasha:
        attribute_function MultiPickers([PiercingsPicker, DickPicker, HaircutPicker], npcs=[bree, minami, samantha, sasha])
        attribute cumshot
        attribute breesuck
        attribute breeinmouth
        attribute minamisuck
        attribute minamiinmouth
        attribute samanthasuck
        attribute samanthainmouth
        attribute sashasuck
        attribute sashainmouth

        always:
            "bj_breeminamisamsasha_bg"
        always:
            "bj_breeminamisamsasha_body"

        group multiple auto variant bree_piercings
        always:
            if_any "breeonmouth"
            "bj_breeminamisamsasha_bree_exp_breeopen"
        group bree_exp auto:
            if_not "breeonmouth"
            attribute breenormal default

        always:
            if_any "minami_haircut"
            "bj_breeminamisamsasha_minami_blonde"
        group multiple auto variant minami_piercings
        always:
            if_all ["minamionmouth", "minami_nohaircut"]
            "bj_breeminamisamsasha_minami_exp_nohaircut_minamiopen"
        group minami_exp auto variant "nohaircut" if_any "minami_nohaircut":
            if_not "minamionmouth"
            attribute minaminormal default

        always:
            if_all ["minamionmouth", "minami_haircut"]
            "bj_breeminamisamsasha_minami_exp_haircut_minamiopen"
        group minami_exp auto variant "haircut" if_any "minami_haircut":
            if_not "minamionmouth"
            attribute minaminormal default

        group multiple auto variant samantha_piercings
        always:
            if_any "samanthaonmouth"
            "bj_breeminamisamsasha_samantha_exp_samanthaopen"
        group samantha_exp auto:
            if_not "samanthaonmouth"
            attribute samanthanormal default

        always:
            if_any "sasha_haircut"
            "bj_breeminamisamsasha_sasha_blonde"
        group multiple auto variant sasha_piercings
        always:
            if_any "sashaonmouth"
            "bj_breeminamisamsasha_sasha_exp_sashaopen"
        group sasha_exp auto:
            if_not "sashaonmouth"
            attribute sashanormal default

        group dick auto:
            if_not ["cumshot", "breesuck", "breeinmouth", "minamisuck", "minamiinmouth", "samanthasuck", "samanthainmouth", "sashasuck", "sashainmouth"]

        always:
            if_any ["cumshot"]
            "bj_breeminamisamsasha_dick_big"

        always:
            if_any ["small", "medium", "big", "cumshot"]
            if_not ["breesuck", "breeinmouth", "minamisuck", "minamiinmouth", "samanthasuck", "samanthainmouth", "sashasuck", "sashainmouth"]
            "bj_breeminamisamsasha_mike_body_center"

        always:
            if_any ["sashasuck", "sashainmouth"]
            "bj_breeminamisamsasha_mike_body_center"

        always:
            if_any ["breesuck", "breeinmouth", "minamisuck", "minamiinmouth"]
            "bj_breeminamisamsasha_mike_body_left"

        always:
            if_any ["samanthasuck", "samanthainmouth"]
            "bj_breeminamisamsasha_mike_body_right"

        always:
            if_any ["breesuck", "breeinmouth"]
            if_not ["minamisuck", "minamiinmouth", "sashasuck", "sashainmouth", "samanthasuck", "samanthainmouth"]
            "bj_breeminamisamsasha_breesuck"

        always:
            if_any ["minamisuck", "minamiinmouth"]
            if_not ["breesuck", "breeinmouth", "sashasuck", "sashainmouth", "samanthasuck", "samanthainmouth"]
            "bj_breeminamisamsasha_minamisuck"

        always:
            if_any ["samanthasuck", "samanthainmouth"]
            if_not ["breesuck", "breeinmouth", "minamisuck", "minamiinmouth", "sashasuck", "sashainmouth"]
            "bj_breeminamisamsasha_samanthasuck"

        always:
            if_any ["sashasuck", "sashainmouth"]
            if_not ["breesuck", "breeinmouth", "minamisuck", "minamiinmouth","samanthasuck", "samanthainmouth"]
            "bj_breeminamisamsasha_sashasuck"

        group multiple auto variant cum

    layeredimage bj breeminamisasha:
        attribute_function MultiPickers([HaircutPicker, DickPicker], append_npc_from_attributes=True)

        attribute nobree null
        attribute nohandsbree null
        attribute nosasha null
        attribute nohandssasha null
        attribute nominami null
        attribute nohandsminami null

        always:
            "bj_breeminamisasha_bg"


        attribute bree
        group breeeye auto if_any ["bree"]:
            attribute breenormal default
        group breemouth auto if_any ["bree"]:
            attribute breesmile default


        attribute sasha
        group sashaeye auto if_any ["sasha"]:
            attribute sashanormal default
        attribute sasha_haircut if_any ["sasha"]
        group sashamouth auto if_any ["sasha"]:
            attribute sashasmile default


        attribute minami null
        attribute minami_nohaircut if_any ["minami"]
        attribute minami_haircut if_any ["minami"]
        group minamieye auto if_any ["minami"]
        group minamimouth auto if_any ["minami"]:
            attribute minaminormal default


        always:
            "bj_breeminamisasha_body_mike"


        group dick auto if_not ["breeonmouth", "minamionmouth", "sashaonmouth"]
        group dick auto variant "outside" if_not ["breeonmouth", "minamionmouth", "sashaonmouth", "sashaside", "breeside", "minamiside"]


        group onmouth auto


        group multiple auto variant cum


        group minamihand auto if_any ["minami"] if_not ["nohandsminami", "breehand", "sashahand"]:
            attribute tobree default
        attribute breehand if_any ["bree"] if_not ["nohandsbree", "minamihand", "sashahand"]
        attribute sashahand if_any ["sasha"] if_not ["nohandssasha", "minamihand", "breehand"]

    layeredimage bj breeminamisasha2:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, DickPicker], npcs=[bree,minami,sasha])


        always:
            "bj_breeminamisasha2_bg"


        attribute bree if_any ["minami"]


        attribute bree_nose if_all ["bree", "minami"]


        attribute breeblush if_all ["bree", "minami"]


        group exp_bree auto if_all ["bree", "minami"]:
            attribute breenormal default
            attribute breewink
            attribute breesurprised


        attribute minami


        attribute minami_nose if_any ["minami"]


        attribute minami_collar if_any ["minami"]


        group eyes auto if_any ["minami"]:
            attribute eyesopen default
            attribute eyesclose


        attribute minami_haircut if_any ["minami"]
        attribute minami_nohaircut if_any ["minami"]


        always:
            if_all ["bree", "minami"] if_not ["blowjob"]
            "bj_breeminamisasha2_bree_righthand"


        attribute facecum null
        group facecum auto if_all ["facecum", "minami"]


        group mouth auto if_any ["minami"] if_not ["blowjob"]:
            attribute normal default
            attribute open
            attribute swallow


        attribute mouthcum null
        group mouthcum auto if_all ["mouthcum", "minami"] if_not ["blowjob"]


        always:
            "bj_breeminamisasha2_mike"


        always:
            if_all ["bree", "minami"]
            "bj_breeminamisasha2_bree_lefthand"


        always:
            if_all ["sasha", "minami"]
            "bj_breeminamisasha2_sasha_lefthand"


        always:
            if_all ["sasha", "minami"]
            if_not ["bree"]
            "bj_breeminamisasha2_sasha_righthand"


        attribute sasha


        attribute sasha_collar if_any ["sasha"]


        attribute sashablush if_any ["sasha"]


        group exp_sasha auto if_any ["sasha"]:
            attribute sashanormal default
            attribute sashaevil
            attribute sashaworried
            attribute sashasurprised


        attribute sasha_haircut if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]


        attribute sasha_nose if_any ["sasha"]
        attribute sasha_ears if_any ["sasha"]


        group dick auto if_not ["blowjob"]


        attribute dickcum null
        group dickcum auto if_any ["dickcum"] if_not ["blowjob"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["blowjob"]


        attribute blowjob if_any ["minami"]


        group cum auto if_all ["cumshot", "minami"]


        attribute leash if_all ["minami_collar", "minami"]

    layeredimage bj breesamsasha:
        attribute_function MultiPickers([CollarPicker, HaircutPicker], npcs=[bree, samantha, sasha])

        attribute bree null
        attribute samantha null
        attribute sasha null

        attribute cumshot null

        always:
            "bj_breesamsasha_bg"
        always:
            "bj_breesamsasha_body"

        attribute bree_nohaircut null
        attribute samantha_nohaircut null


        group multiple auto variant collars
        group bree_exp auto:
            if_not ["breesuck", "breeballsuck"]
            attribute breenormal default

        group samantha_exp auto:
            if_not ["samanthasuck"]
            attribute samanthanormal default

        attribute sasha_nohaircut null
        attribute sasha_haircut
        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        group sasha_exp auto:
            if_not ["sashasuck", "sashaballsuck"]
            attribute sashanormal default

        always:
            if_not ["cumshot", "onface"]
            "bj_breesamsasha_mike_body"
        always:
            if_any ["cumshot", "onface"]
            "bj_breesamsasha_dick_cumshot"

        group dick auto:
            if_not ["cumshot", "onface", "breesuck", "samanthasuck", "sashasuck"]
            attribute medium default

        group cum auto:
            attribute inmouth null

        group multiple auto variant ballsuck
        group suck auto
        group cuminmouth auto if_any "inmouth"

    layeredimage bj breesasha:
        attribute_function MultiPickers([HaircutPicker, PiercingsPicker, CollarPicker], append_npc_from_attributes=True)
        always:
            "bj_breesasha_bg"

        attribute bree

        attribute sasha

        group multiple auto variant collars
        group multiple auto variant piercings

        group multiple auto variant haircuts
        group multiple:
            attribute bree_nohaircut null
            attribute sasha_nohaircut null

        group dick auto:
            attribute normal default
            attribute nodick null

        group breeexp auto if_any "bree":
            attribute breeopen default

        group sashaexp auto if_any "sasha":
            attribute sashaopen default

        group hand auto

        attribute breecumtongue:
            "bj_breesasha_bree_cum_tongue"

        attribute breecummouth:
            "bj_breesasha_bree_cum_mouth"

        attribute breefacial:
            "bj_breesasha_bree_facial"

        attribute breesaliva:
            "bj_breesasha_bree_saliva"

        attribute sashacumtongue:
            "bj_breesasha_sasha_cum_tongue"

        attribute sashacummouth:
            "bj_breesasha_sasha_cum_tongue"

        attribute sashafacial:
            if_any "nodick"
            "bj_breesasha_sasha_facial_nodick"

        attribute sashafacial:
            if_not "nodick"
            "bj_breesasha_sasha_facial"

        attribute sashasaliva:
            "bj_breesasha_sasha_saliva"

        attribute cumshare

        attribute cumshot

        attribute wet

    layeredimage bj leximinamisam:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, PubesPicker], npcs=["lexi", minami, samantha])

        group bg auto:
            attribute beach default

        group lexi if_any ["lexifront", "lexiright"]:
            attribute lexi default null

        group lexilocation auto if_not ["lexifront"]

        group pubes auto variant "lexiright" if_any ["lexiright"] if_not ["lexifront"]
        group pregnancy auto variant "lexiright" if_any ["lexiright"] if_not ["lexifront"]
        group collars auto variant "lexiright" if_any ["lexiright"] if_not ["lexifront"]
        group multiple auto variant piercing_lexiright when lexiright and not lexifront

        group minami if_any ["minamifront", "minamileft"]:
            attribute minami default null

        group minamilocation auto if_not ["minamifront"]

        group pubes auto variant "minamileft" if_any ["minamileft"] if_not ["minamifront"]
        group pregnancy auto variant "minamileft" if_any ["minamileft"] if_not ["minamifront"]
        group haircuts auto variant "minamileft" if_any ["minamileft"] if_not ["minamifront"]
        group collars auto variant "minamileft" if_any ["minamileft"] if_not ["minamifront"]
        group multiple auto variant piercing_minamileft when minamileft and not minamifront

        group samantha if_any ["samanthafront", "samantharight", "samanthaleft"]:
            attribute samantha default null

        group samanthalocation auto if_not ["samanthafront"]

        group pubes auto variant "samanthaleft" if_any ["samanthaleft"] if_not ["samantharight", "samanthafront"]
        group pregnancy auto variant "samanthaleft" if_any ["samanthaleft"] if_not ["samantharight", "samanthafront"]
        group collars auto variant "samanthaleft" if_any ["samanthaleft"] if_not ["samantharight", "samanthafront"]
        group multiple auto variant piercing_samanthaleft when samanthaleft and not (samantharight or samanthafront)

        group pubes auto variant "samantharight" if_any ["samantharight"] if_not ["samanthaleft", "samanthafront"]
        group pregnancy auto variant "samantharight" if_any ["samantharight"] if_not ["samanthaleft", "samanthafront"]
        group collars auto variant "samantharight" if_any ["samantharight"] if_not ["samanthaleft", "samanthafront"]
        group multiple auto variant piercing_samantharight when samantharight and not (samanthaleft or samanthafront)

        always:
            "bj_leximinamisam_mike"

        group lexilocation auto if_any ["lexifront"]

        group minamilocation auto if_any ["minamifront"]

        group samanthalocation auto if_any ["samanthafront"]

        group fx auto variant "lexifront" if_any ["lexifront"]
        group fx auto variant "minamifront" if_any ["minamifront"]
        group fx auto variant "samanthafront" if_any ["samanthafront"]

        group lexihead auto if_any ["lexifront"]
        group minamihead auto if_any ["minamifront"]
        group samanthahead auto if_any ["samanthafront"]

        group exp auto variant "lexifront" if_any ["lexifront"] if_not ["lexiright"]:
            attribute normal default
        group multiple auto variant piercing_lexifront when lexifront and not lexiright

        group haircuts auto variant "minamifront" if_any ["minamifront"] if_not ["minamileft"]
        group exp auto variant "minamifront" if_any ["minamifront"] if_not ["minamileft"]:
            attribute normal default
        group multiple auto variant piercing_minamifront when minamifront and not minamileft

        group exp auto variant "samanthafront" if_any ["samanthafront"] if_not ["samantharight", "samanthaleft"]:
            attribute normal default
        group multiple auto variant piercing_samanthafront when samanthafront and not (samantharight or samanthaleft)

        group dick auto variant "lexifront" if_any ["lexifront"] if_not ["lexiright"]
        group dick auto variant "minamifront" if_any ["minamifront"] if_not ["minamileft"]
        group dick auto variant "samanthafront" if_any ["samanthafront"] if_not ["samantharight", "samanthaleft"]

        attribute cum null
        group cum auto variant "lexiright" if_all ["lexiright", "cum"] if_not ["lexifront"]
        group cum auto variant "lexifront" if_all ["lexifront", "cum"] if_not ["lexiright"]

        group cum auto variant "minamileft" if_all ["minamileft", "cum"] if_not ["minamifront"]
        group cum auto variant "minamifront" if_all ["minamifront", "cum"] if_not ["minamileft"]

        group cum auto variant "samantharight" if_all ["samantharight", "cum"] if_not ["samanthafront", "samanthaleft"]
        group cum auto variant "samanthaleft" if_all ["samanthaleft", "cum"] if_not ["samanthafront", "samantharight"]
        group cum auto variant "samanthafront" if_all ["samanthafront", "cum"] if_not ["samantharight", "samanthaleft"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        group fg auto

    layeredimage breesasha ending:
        attribute_function MultiPickers([CollarPicker, HaircutPicker, EndingKidPicker], npcs=[bree, sasha])

        attribute bree null
        attribute sasha null

        always "breesasha_ending_bree"
        attribute sasha_haircut
        attribute sasha_nohaircut
        attribute sasha_boobjob
        group multiple auto variant collars
        always "breesasha_ending_mike"


        group multiple auto variant kids

    layeredimage breesasha kiss:
        attribute_function MultiPickers([OutfitPicker, HaircutPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npcs=[bree, sasha], add_simple_outfit_attribute=True)


        always "breesasha_kiss_base"

        group arms auto if_not ["naked"]


        group multiple auto variant pregnancy


        attribute sasha_boobjob


        group hairs auto


        group multiple auto variant piercings


        attribute naked null
        attribute topless null
        group multiple auto variant outfits when not (boobjob or naked or topless)
        group multiple auto variant outfits_boobjob when boobjob and not (naked or topless)
        group multiple auto variant outfits_pregnant when pregnant and not (boobjob or naked or topless)
        group multiple auto variant outfits_boobjob_pregnant when boobjob and pregnant and not (naked or topless)

        group multiple auto variant collars when not rpg

        attribute cum

    layeredimage couch fun:
        attribute_function MultiPickers([PiercingsPicker], append_npc_from_attributes=True)
        attribute facial null
        attribute masturbate null

        always:
            "couch_fun_bg"
        always:
            "couch_fun_dick_masturbate"

        group masturbate auto if_any ["masturbate"]:
            attribute up default

        attribute sasha

        always:
            if_all ["sasha", "facial"]
            "couch_fun_sasha_facial"

        always:
            if_not "masturbate"
            "couch_fun_dick_bj"

        attribute bree

        group multiple auto variant piercings

        always:
            if_all ["bree","facial"]
            "couch_fun_bree_facial"

        attribute precum
        attribute cumshot:
            "couch_fun_cumshot"

    layeredimage cumshot breesamsasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker], npcs=[bree, samantha, sasha])

        attribute bree null
        attribute samantha null
        attribute sasha null

        attribute bree_nohaircut null
        attribute samantha_nohaircut null

        attribute sasha_boobjob null
        attribute sasha_noboobjob null

        always:
            "cumshot_breesamsasha_bg"
        always:
            "cumshot_breesamsasha_body"

        attribute sasha_nohaircut
        attribute sasha_haircut null
        group multiple auto variant collars
        group multiple auto variant piercings
        group multiple:
            attribute bree_clit null
            attribute bree_ears null
            attribute bree_lips null
            attribute bree_navel null
            attribute bree_pregnant_navel null
            attribute bree_nipples null
            attribute bree_tongue null
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_navel null
            attribute samantha_pregnant_navel null
            attribute samantha_nipples null
            attribute samantha_tongue null
            attribute sasha_clit null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_nipples null
            attribute sasha_tongue null


        always:
            "cumshot_breesamsasha_dick"

        group multiple auto variant cum

    layeredimage cumshot breesasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, HaircutPicker], npcs=[bree, sasha])


        always:
            "cumshot_breesasha_bg"


        attribute sasha


        attribute bree


        group pregnancy auto


        group collars auto


        group exp_bree auto:
            attribute breehappy default
            attribute breesurprised
            attribute breepleasure


        always:
            "cumshot_breesasha_bree_righthand"


        group poses auto:
            attribute normal default null
            attribute blow null
            attribute lick null


        group nohaircut auto if_any ["nohaircut", "sasha_nohaircut"]
        group haircut auto if_any ["haircut", "sasha_haircut"]


        group boobjob auto if_any ["boobjob", "sasha_boobjob"]


        group collars auto variant "normal" if_any ["normal"]
        group collars auto variant "blow" if_any ["blow"]
        group collars auto variant "lick" if_any ["lick"]


        group exp_sasha auto variant "normal" if_any ["normal"]:
            attribute sashahappy default
            attribute sashapleasure
        group exp_sasha auto variant "lick" if_any ["lick"]:
            attribute swallow default
            attribute tongueout


        group eyes_sasha auto variant "blow" if_any ["blow"]:
            attribute opened default
            attribute closed


        group sasha_mouth auto variant "noblowjob" if_not ["blowjob"]


        attribute cum null
        group multiple auto variant cum_sasha_normal when cum and normal 
        group multiple auto variant cum_sasha_blow when cum and blow 
        group multiple auto variant cum_sasha_bree when cum 
        group multiple auto variant cum_sasha_lick when cum and lick 


        always:
            if_not ["lick"]
            "cumshot_breesasha_bree_tit"


        group multiple auto variant cum_bree when cum 


        group dick auto:
            attribute hard default
            attribute limp


        attribute dickcum null
        group dickcum auto if_any ["dickcum"]


        attribute cumshoot null
        group cumshoot auto if_any ["cumshoot"]


        attribute blowjob null
        group sasha_mouth auto variant "blowjob" if_any ["blowjob"]


        attribute creampie null
        group creampie auto if_all ["creampie", "hard"]


        attribute handjob null
        group handjob auto if_any ["handjob"]


        group mikehand auto


        group leash_sasha auto if_all ["leash", "sasha_collar"]


        always:
            if_all ["leash", "bree_collar"]
            "cumshot_breesasha_leash_bree"


        group handle auto

    layeredimage fivesome breeminamisamsasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[bree, minami, samantha, sasha])
        attribute condom
        always:
            "fivesome_breeminamisamsasha_bg"
        always:
            "fivesome_breeminamisamsasha_body"

        always:
            "fivesome_breeminamisamsasha_mike_body"

        group fx auto
        attribute sasha_boobjob


        group multiple auto variant pregnancy
        group multiple auto variant collars
        group multiple auto variant piercings
        group multiple auto variant piercings_novaginal when not vaginal
        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings_boobjob when sasha_boobjob
        group multiple auto variant piercings_noboobjob when not sasha_boobjob
        group multiple auto variant haircuts

        group bree_exp auto:
            attribute breelookup default

        group minami_exp auto variant "nohaircut" if_not "minami_haircut":
            attribute minamilookup default
        group minami_exp auto variant "haircut" if_any "minami_haircut":
            attribute minamilookup default

        group samanthafuck auto
        group samanthafuck auto variant "condom" if_any "condom"
        attribute samantha_pubes

        group samantha_exp auto:
            attribute samanthalookup default

        group sasha_exp auto:
            attribute sashalookup default

        group multiple auto variant cum

        group dick auto:
            if_not ["anal", "condom", "cumshot", "incondom", "vaginal", "samanthaanal", "samanthavaginal"]
        always:
            if_any ["condom", "cumshot", "incondom"]
            if_not ["anal", "vaginal", "samanthaanal", "samanthavaginal"]
            "fivesome_breeminamisamsasha_dick_big"
        always:
            if_any ["condom"]
            if_not ["anal", "cumshot", "vaginal", "samanthaanal", "samanthavaginal", "incondom"]
            "fivesome_breeminamisamsasha_dick_condom_big"

    layeredimage foursome breeminamisasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker], npcs=[bree, minami, sasha])

        attribute bree null
        attribute minami null
        attribute sasha null

        always:
            "foursome_breeminamisasha_bg"
        always:
            "foursome_breeminamisasha_body"

        group multiple auto variant pregnancy

        attribute sasha_noboobjob null
        attribute sasha_boobjob null

        group boobjobs auto variant "pregnant" if_all ["sasha_boobjob", "sasha_pregnant"]
        group boobjobs auto variant "nopregnant" if_any "sasha_boobjob" if_not "sasha_pregnant"

        group multiple auto variant piercings
        group multiple:
            attribute bree_ears null
            attribute bree_clit null
            attribute bree_lips null
            attribute bree_tongue null
            attribute minami_clit null
            attribute minami_ears null
            attribute sasha_lips null
            attribute sasha_tongue null
        group piercings auto variant "boobjob" if_any "sasha_boobjob"
        group piercings auto variant "noboobjob" if_not "sasha_boobjob"

        group multiple auto variant collars

        group multiple auto variant haircuts
        group multiple:
            attribute bree_nohaircut null
            attribute minami_nohaircut null
            attribute sasha_nohaircut null

        group bree_exp auto:
            attribute breepleasure default
        group bree_fx auto

        group minami_exp auto:
            attribute minamipleasure default
        group minami_fx auto

        group sasha_exp auto:
            attribute sashapleasure default
        group sasha_fx auto

    layeredimage foursome breesamsasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, DickPicker, PregnancyPicker, PubesPicker], npcs=[bree, samantha, sasha])
        always:
            "foursome_breesamsasha_bg"
        always:
            "foursome_breesamsasha_body"

        attribute bree_nohaircut null
        attribute samantha_nohaircut null
        attribute sasha_nohaircut null

        attribute bree_pubes null
        attribute sasha_pubes null

        group multiple auto variant pregnancy

        group multiple auto variant piercings
        group multiple:
            attribute bree_clit null
            attribute bree_ears null
            attribute bree_lips null
            attribute bree_navel null
            attribute bree_pregnant_navel null
            attribute bree_nipples null
            attribute bree_tongue null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_tongue null
            attribute sasha_ears null
            attribute sasha_lips null
            attribute sasha_nipples null
            attribute sasha_tongue null

        group piercings auto variant "vaginal" if_any "vaginal"
        group piercings auto variant "novaginal" if_not "vaginal"

        group multiple auto variant collars
        group multiple:
            attribute bree_collar null

        group bree_exp auto:
            attribute breenormal default

        group samanthafuck auto
        attribute samantha_pubes
        group samantha_exp auto:
            attribute samanthanormal default

        attribute sasha_haircut
        attribute sasha_boobjob
        group sasha_exp auto:
            attribute sashanormal default

        group multiple auto variant cum

        group dick auto:
            if_not ["vaginal", "anal", "tease"]
        group fx auto:
            if_not ["vaginal", "anal"]

        group multiple auto variant finger

    layeredimage foursome leximinamisam:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, DickPicker, OutfitPicker, CollarPicker, HaircutPicker], append_npc_from_attributes=True)

        group bg auto:
            attribute bedroom default

        attribute minami default

        always:
            if_any "samantha"
            "foursome_leximinamisam_samantha_legback"

        always:
            if_any "samantha"
            "foursome_leximinamisam_samantha_shadow"

        attribute lexi

        group multiple auto variant pregnancy

        group multiple auto variant collars
        group multiple auto variant piercings_minami
        group multiple auto variant piercings_lexi when lexi

        attribute lexifingering

        always:
            if_any "samantha"
            "foursome_leximinamisam_samantha_lexishadow"

        attribute samantha

        attribute samantha_pregnant

        group multiple auto variant piercings_samantha when samantha

        attribute samantha_collar

        group exp_minami auto:
            attribute normal default

        group haircuts auto

        group dick_outside auto if_not ["vaginal", "anal"]
        group dick_inside auto if_any ["vaginal", "anal"]

        always:
            "foursome_leximinamisam_balls"

        attribute cum null
        group dickcum auto if_all ["cum"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot"]

        attribute creampie

        attribute condom null
        group condom_outside auto if_all ["condom"] if_not ["vaginal", "anal"]
        group condom_inside auto if_all ["condom", "mike", "vaginal"]

        group condomcum auto if_all ["condom", "cum"] if_not ["vaginal", "anal"]

        attribute speed

        always:
            "foursome_leximinamisam_fg"

    layeredimage foursome lexisamsasha:
        attribute_function MultiPickers([HaircutPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=["lexi", samantha, sasha])
        attribute lollipop
        always:
            "foursome_lexisamsasha_bg"
        always:
            "foursome_lexisamsasha_body"
        attribute sasha_haircut
        group multiple auto variant pregnancy
        group multiple auto variant piercings
        group piercings auto variant "boobjob" if_any "sasha_boobjob"
        group piercings auto variant "noboobjob" if_not "sasha_boobjob"
        group multiple auto variant collars
        attribute sasha_boobjob
        group lexi_exp auto:
            attribute lexinormal default
        group lexi_fx auto
        always:
            if_any "lollipop"
            "foursome_lexisamsasha_lexi_lollipop"

        group samantha_exp auto:
            attribute samanthanormal default
        group samantha_fx auto

        group sasha_exp auto:
            attribute sashanormal default
        group sasha_fx auto

        group cum auto

    layeredimage girls couch fun:
        attribute_function MultiPickers([HaircutPicker, PregnancyPicker, CollarPicker, PiercingsPicker], append_npc_from_attributes=True)
        attribute bree null
        attribute minami null
        attribute samantha null
        attribute sasha null

        attribute sasha_boobjob null
        attribute sasha_noboobjob null

        always "girls_couch_fun_bg"
        always "girls_couch_fun_bodies"

        attribute lexi

        group multiple auto variant collars
        group multiple:
            attribute bree_collar null
        attribute lexi_collar if_any ["lexi"]

        group multiple auto variant pregnancies
        attribute lexi_pregnant if_any ["lexi"]

        group multiple auto variant piercings
        group multiple:
            attribute bree_clit null
            attribute bree_ears null
            attribute bree_lips null
            attribute bree_navel null
            attribute bree_pregnant_navel null
            attribute bree_tongue null
            attribute lexi_clit null
            attribute lexi_ears null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_nipples null
            attribute lexi_tongue null
            attribute minami_clit null
            attribute minami_ears null
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_tongue null
            attribute sasha_clit null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_nipples null
            attribute sasha_tongue null

        attribute lexi_nose if_any ["lexi"]

        group multiple auto variant haircuts
        group multiple:
            attribute bree_nohaircut null
            attribute bree_haircut null
            attribute lexi_nohaircut null
            attribute lexi_haircut null
            attribute samantha_nohaircut null
            attribute samantha_haircut null
            attribute sasha_haircut null

        always "girls_couch_fun_minami_mouth"

        group multiple auto variant vibrators

    layeredimage home ending:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, DickPicker, PregnancyPicker, HaircutPicker], append_npc_from_attributes=True)

        attribute cum


        always:
            "home_ending_bg"


        attribute samantha
        attribute samantha_pregnant
        group multiple auto variant piercings_samantha when samantha or samantha_pregnant
        group multiple auto variant cum_samantha when cum and (samantha or samantha_pregnant)


        attribute samantha_collar


        always:
            "home_ending_mike"


        always:
            if_any ["samantha", "samantha_pregnant"]
            "home_ending_hand_samantha"


        attribute bree
        attribute bree_pregnant


        attribute sasha
        attribute sasha_pregnant
        attribute sasha_nohaircut


        attribute minami


        group dick auto


        attribute lexi
        attribute lexi_pregnant


        group multiple auto variant exp


        attribute minami_haircut


        attribute sasha_collar


        group multiple auto variant piercings_bree when bree or bree_pregnant
        group multiple auto variant piercings_lexi when lexi or lexi_pregnant
        group multiple auto variant piercings_minami when minami or minami_pregnant
        group multiple auto variant piercings_sasha when sasha or sasha_pregnant


        group cumdick auto if_any ["cum"]


        group multiple auto variant cum_bree when cum and (bree or bree_pregnant)
        group multiple auto variant cum_lexi when cum and (lexi or lexi_pregnant)
        group multiple auto variant cum_minami when cum and (minami or minami_pregnant)
        group multiple auto variant cum_sasha when cum and (sasha or sasha_pregnant)


        attribute glasses


        always:
            "home_ending_fg"

    layeredimage lesbian sex breesam:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, HaircutPicker], npcs=[bree, samantha])


        always "lesbian_sex_breesam_bg"
        always "lesbian_sex_breesam_bodies"


        group multiple auto variant collars


        attribute strapon

        group multiple auto variant piercings_back

        group multiple auto variant pregnancy


        group multiple auto variant piercings


        group exp auto:
            attribute pleasure default


        always "lesbian_sex_breesam_fg"

    layeredimage lesbian sex minsam:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, PiercingsPicker, CollarPicker, HaircutPicker], npcs=[minami, samantha])


        always "lesbian_sex_minsam_bg"
        always "lesbian_sex_minsam_bodies"


        group pubic auto
        group pregnancy auto
        group multiple auto variant piercings
        group collars auto
        group hair auto


        attribute vibrator


        always "lesbian_sex_minsam_light"

    layeredimage lesbian sex samlexi:
        attribute_function MultiPickers([PubesPicker, PregnancyPicker, CollarPicker, PiercingsPicker], npcs=["lexi", samantha])


        always "lesbian_sex_samlexi_bg"
        always "lesbian_sex_samlexi_bodies"


        group expsam auto:
            attribute sampleasure default
        group explexi auto:
            attribute lexismile default


        attribute vibratorsam
        attribute vibratorlexi


        group pubic auto
        group pregnancy auto
        group collars auto
        group multiple auto variant piercings


        always "lesbian_sex_samlexi_light"


        attribute squirt

    layeredimage lesbian sex samsasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, PregnancyPicker, HaircutPicker], npcs=[samantha, sasha])


        always "lesbian_sex_samsasha_bg"
        always "lesbian_sex_samsasha_bodies"


        group collars auto


        attribute sasha_clit
        attribute strapon
        attribute samantha_clit


        attribute cum


        group pregnancy auto


        attribute sasha_boobjob


        group multiple auto variant piercings
        group multiple auto variant piercings_bb when bb
        group multiple auto variant piercings_nobb when not sasha_boobjob


        group exp auto:
            attribute normal default


        group hair auto


        attribute sasha_ears


        always "lesbian_sex_samsasha_fg"

    layeredimage sandwich breeminami:
        attribute_function MultiPickers([PubesPicker, PiercingsPicker, HaircutPicker, DickPicker], npcs=[bree, minami])


        always:
            "sandwich_breeminami_bg"


        always:
            "sandwich_breeminami_bodies"


        attribute cumbody


        group multiple auto variant pubic



        group exp_bree auto:
            attribute breenormal default

        group exp_minami auto:
            attribute minaminormal default


        attribute minami_nohaircut
        attribute minami_haircut


        attribute tongueout


        group multiple auto variant piercings
        group multiple auto variant piercings_tongueout when tongueout


        attribute dripcum


        attribute cumshare


        always if_any ["mike"] if_not ["onface", "lick"]:
            "sandwich_breeminami_mikehand"


        group dildo:
            attribute dildodouble if_any ["outside", "onface", "lick"]
            attribute dildodouble if_all ["breefuck", "anal"]
            attribute dildodouble if_all ["minamifuck", "anal"]
            attribute dildobree if_not ["breefuck", "beadsbree"]
            attribute dildominami if_not ["minamifuck", "beadsminami"]


        attribute beadsbree if_any ["outside", "onface", "lick", "minamifuck"]
        attribute beadsbree if_all ["breefuck", "vaginal"]
        attribute beadsminami if_any ["outside", "onface", "lick", "breefuck"]
        attribute beadsminami if_all ["minamifuck", "vaginal"]


        attribute onface if_any ["mike"] if_not ["outside", "breefuck", "minamifuck", "lick"]
        group fuck if_any ["mike"]:
            attribute outside null default
            attribute breefuck null
            attribute minamifuck null
            attribute onface null
            attribute lick null


        attribute creampie null
        group minamifuck auto if_all ["mike", "minamifuck"]:
            attribute vaginal default
        group minamifuck auto variant "creampie" if_all ["mike", "minamifuck", "creampie"] if_not ["condom"]:
            attribute vaginal default
        group minamifuck auto variant "condom" if_all ["mike", "minamifuck", "condom"]:
            attribute vaginal default


        attribute creampie null
        group breefuck auto if_all ["mike", "breefuck"]:
            attribute vaginal default
        group breefuck auto variant "creampie" if_all ["mike", "breefuck", "creampie"] if_not ["condom"]:
            attribute vaginal default
        group breefuck auto variant "condom" if_all ["mike", "breefuck", "condom"]:
            attribute vaginal default


        group onface auto variant "condom" if_all ["mike", "onface", "condom"] if_not ["cumshot"]


        group onface auto variant "cumshot" if_all ["mike", "onface", "cumshot"] if_not ["condom"]


        group onface auto variant "condomcum" if_all ["mike", "onface", "condom", "cumshot"]


        group outside auto if_all ["mike", "outside"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "outside", "cumshot"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto if_all ["mike", "outside", "dickcum"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "outside", "condom"] if_not ["cumshot"]


        group condomcum auto if_all ["mike", "outside", "cumshot", "condom"]


        attribute mike null
        group mike auto if_all ["mike"] if_any ["outside", "breefuck", "minamifuck"]:
            attribute shallow default


        group lick auto if_all ["mike", "lick"]:
            attribute lickboobs default

    layeredimage sandwich minamisasha:
        attribute_function MultiPickers([PiercingsPicker, PubesPicker, HaircutPicker, DickPicker], npcs=[sasha, minami])


        always:
            "sandwich_minamisasha_bg"


        always:
            "sandwich_minamisasha_bodies"


        group multiple auto variant pubic


        group multiple auto variant piercings
        group multiple auto variant piercings_nodildo when not dildo


        attribute sasha_boobjob


        group eyes_minami auto:
            attribute minaminormal default


        group eyes_sasha auto:
            attribute sashanormal default


        group sashahair auto


        group minamihair auto


        attribute facecum
        attribute bodycum


        group dild auto if_all ["mike", "fuckminami"] if_not ["vaginal"]
        group dild auto if_all ["mike", "fucksasha"] if_not ["vaginal"]
        group dild auto if_any ["fuckminami", "fucksasha"] if_not ["mike"]
        group dild auto if_not ["fuckminami", "fucksasha"]
        group multiple auto variant piercings_dildo when dildo


        always:
            "sandwich_minamisasha_sheets"



        group sas_beads if_all ["mike", "fucksasha"]:
            attribute sashabeads if_not ["anal"]
        group sas_beads:
            attribute sashabeads if_not ["mike"]
            attribute sashabeads if_not ["fucksasha"]

        group min_beads if_all ["mike", "fuckminami"]:
            attribute minamibeads if_not ["anal"]
        group min_beads:
            attribute minamibeads if_not ["mike"]
            attribute minamibeads if_not ["fuckminami"]


        attribute mike null
        group mike if_any ["mike"]:
            attribute lickpussysasha
            attribute lickasssasha
            attribute lickpussyminami
            attribute lickassminami
            attribute fuckminami
            attribute fucksasha
            attribute wank default


        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group cumshot auto variant "fuckminami" if_all ["mike", "fuckminami", "cumshot"] if_not ["condom"]


        group dick auto variant "fuckminami" if_all ["mike", "fuckminami"]
        group dick auto variant "fucksasha_out" if_all ["mike", "fucksasha", "out"]
        group dick auto variant "fucksasha" if_all ["mike", "fucksasha"]
        group dick auto variant "wank" if_all ["mike", "wank"]


        attribute cumshot null
        group cumshot auto variant "fucksasha_out" if_all ["mike", "fucksasha", "out", "cumshot"] if_not ["condom"]
        group cumshot auto variant "wank" if_all ["mike", "wank", "cumshot"] if_not ["condom"]


        attribute dickcum null
        group dickcum auto variant "fucksasha_out" if_all ["mike", "fucksasha", "out", "dickcum"] if_not ["condom"]
        group dickcum auto variant "wank" if_all ["mike", "wank", "dickcum"] if_not ["condom"]


        attribute creampie null
        group creampie auto variant "fuckminami" if_all ["mike", "fuckminami", "creampie"] if_not ["condom"]
        group creampie auto variant "fucksasha" if_all ["mike", "fucksasha", "creampie"] if_not ["condom"]


        attribute condom null
        group condom auto variant "fuckminami" if_all ["mike", "fuckminami", "condom"]
        group condom auto variant "fucksasha_out" if_all ["mike", "fucksasha", "out", "condom"] if_not ["cumshot"]
        group condom auto variant "fucksasha" if_all ["mike", "fucksasha", "condom"]
        group condom auto variant "wank" if_all ["mike", "wank", "condom"]


        group condomcum auto variant "fucksasha_out" if_all ["mike", "fucksasha", "out", "condom", "cumshot"]
        group condomcum auto variant "wank" if_all ["mike", "wank", "condom", "cumshot"]


        group mikehand auto variant "fucksasha" if_all ["mike", "fucksasha"]:
            attribute hold if_any ["anal", "vaginal"]
            attribute stroke if_any ["out"]
        group mikehand auto variant "wank" if_all ["mike", "wank"]


        always:
            if_all ["mike", "fucksasha", "out", "dickcum", "stroke"]
            "sandwich_minamisasha_cumonhand_fucksasha"
        always:
            if_all ["mike", "wank", "dickcum", "stroke"]
            "sandwich_minamisasha_cumonhand_wank"

    layeredimage shower bj breesasha:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, CollarPicker, HaircutPicker], append_npc_from_attributes=True)
        always:
            "shower_bj_breesasha_bg"
        always:
            "shower_bj_breesasha_mike_leg"

        attribute sasha
        attribute sasha_pregnant
        attribute sasha_noboobjob null
        attribute sasha_boobjob
        attribute sasha_nohaircut
        attribute sasha_haircut null

        always:
            if_any "sasha"
            "shower_bj_breesasha_sasha_hair_line"
        attribute sasha_collar

        group multiple auto variant sasha_piercings
        group multiple:
            attribute sasha_lips null
        group sasha_piercings auto variant "boobjob" if_any "sasha_boobjob"
        group sasha_piercings auto variant "noboobjob" if_not "sasha_boobjob"

        attribute bodycum:
            if_any "sasha"
            "shower_bj_breesasha_sasha_bodycum"
        attribute facial:
            if_any "sasha"
            "shower_bj_breesasha_sasha_facial"

        attribute bree
        attribute bree_nohaircut null
        attribute bree_pregnant

        group multiple auto variant bree_piercings

        attribute bodycum:
            if_any "bree"
            "shower_bj_breesasha_bree_bodycum"

        attribute facial:
            if_any "bree"
            "shower_bj_breesasha_bree_facial"

        attribute cumshot:
            if_any "shoot"
            "shower_bj_breesasha_cumshot"

        always:
            "shower_bj_breesasha_mike"

        group dick auto:
            attribute up default

    layeredimage shower breesasha:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, HaircutPicker, PiercingsPicker], npcs=[bree, sasha])
        always:
            "shower_breesasha_bg"

        attribute bree

        attribute bree_pregnant
        attribute bree_collar
        group multiple auto variant bree_piercings

        attribute sasha
        attribute sasha_pregnant
        attribute sasha_boobjob
        group haircuts auto

        group multiple auto variant sasha_piercings
        group sasha_piercings auto variant "boobjob" if_any "sasha_boobjob"
        group sasha_piercings auto variant "noboobjob" if_not "sasha_boobjob"

        always:
            "shower_breesasha_wet"

    layeredimage shower threesome breesasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker], npcs=[bree, sasha])
        attribute bree null

        attribute sasha null

        always:
            "shower_threesome_breesasha_bg"
        always:
            "shower_threesome_breesasha_arms"
        always:
            "shower_threesome_breesasha_bodies"


        group multiple auto variant collars
        group multiple auto variant piercings
        group multiple:
            attribute bree_ears null
            attribute sasha_ears null

        attribute sasha_boobjob
        attribute sasha_noboobjob null
        group multiple auto variant haircuts
        group multiple:
            attribute bree_nohaircut null

        always:
            "shower_threesome_breesasha_line"
        group multiple auto variant pregnancy

        always:
            "shower_threesome_breesasha_sasha_arm_shadow"
        always:
            "shower_threesome_breesasha_sasha_arm"
        always:
            "shower_threesome_breesasha_wet"

    layeredimage sixsome breeleximinamisamsasha:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker, DickPicker], npcs=[bree, "lexi", minami, samantha, sasha])

        attribute anal null
        attribute vaginal null
        attribute bubblegum null

        always:
            "sixsome_breeleximinamisamsasha_bg"
        always:
            "sixsome_breeleximinamisamsasha_body"

        group multiple auto variant fx
        group multiple auto variant collars
        group multiple auto variant pregnancy
        group multiple auto variant haircuts

        group piercings auto variant "breevaginalgape" if_any "breevaginalgape"
        group piercings auto variant "breenogape" if_not "breevaginalgape"
        group bree_exp auto:
            attribute breenormal default

        group piercings auto variant "lexivaginalgape" if_any "lexivaginalgape"
        group piercings auto variant "lexinogape" if_not "lexivaginalgape"
        group lexi_exp auto:
            attribute lexinormal default
        always:
            if_any "bubblegum"
            "sixsome_breeleximinamisamsasha_lexi_bubblegum"

        group piercings auto variant "minamivaginalgape" if_any "minamivaginalgape"
        group piercings auto variant "minaminogape" if_not "minamivaginalgape"
        group minami_exp auto:
            attribute minaminormal default

        group piercings auto variant "samanthavaginalgape" if_any "samanthavaginalgape"
        group piercings auto variant "samanthanogape" if_not "samanthavaginalgape"
        group samantha_exp auto:
            attribute samanthanormal default

        group piercings auto variant "sashavaginalgape" if_any "sashavaginalgape"
        group piercings auto variant "sashanogape" if_not "sashavaginalgape"
        group sasha_exp auto:
            attribute sashanormal default

        group multiple auto variant gape
        group multiple auto variant cum

        group location auto

        group fuck auto variant "anal" if_any "anal"
        group fuck auto variant "vaginal" if_any "vaginal"

        group dick auto variant "mikebree":
            if_any "mikebree"
            if_not "breefuck"
        group dick auto variant "mikelexi":
            if_any "mikelexi"
            if_not "lexifuck"
        group dick auto variant "mikeminami":
            if_any "mikeminami"
            if_not "minamifuck"
        group dick auto variant "mikesamantha":
            if_any "mikesamantha"
            if_not "samanthafuck"
        group dick auto variant "mikesasha":
            if_any "mikesasha"
            if_not "sashafuck"
        group multiple auto variant fx_dick

    layeredimage smoking pot:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PiercingsPicker, PubesPicker, OutfitPicker, DickPicker, SeasonPicker, MCCGPicker], append_npc_from_attributes=True)

        attribute topless null
        attribute bottomless null
        attribute naked null


        group bg auto:
            attribute livingroom default


        attribute mikemc
        group dick auto if_all ["mikemc"] if_any ["bottomless", "naked"]
        group bot auto variant "mikemc" if_any ["mikemc"] if_not ["bottomless", "naked"]:
            attribute mc_casual default
        group top auto variant "mikemc" if_any ["mikemc"] if_not ["topless", "naked"]


        attribute mike
        group dick auto if_all ["mike"] if_any ["bottomless", "naked"]
        group bot auto variant "mike" if_any ["mike"] if_not ["bottomless", "naked"]:
            attribute mike_casual default
        group top auto variant "mike" if_any ["mike"] if_not ["topless", "naked"]

        group mike_eyes:
            attribute mikeopen default null
            attribute mikeclose null
        group exp_mike auto variant "mikeopen" if_any ["mike", "mikemc"] if_all ["mikeopen"]:
            attribute mikenormal default
        group exp_mike auto variant "mikeclose" if_any ["mike", "mikemc"] if_all ["mikeclose"]


        attribute lexi
        attribute lexi_collar if_any ["lexi"]
        attribute lexi_pregnant if_any ["lexi"]
        group multiple auto variant piercings_lexi when lexi
        group multiple:
            attribute lexi_clit null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_tongue null
        group bot auto variant "lexi" if_any ["lexi"] if_not ["lexi_pregnant", "bottomless", "naked"]
        group top auto variant "lexi" if_any ["lexi"] if_not ["lexi_pregnant", "topless", "naked"]
        group bot auto variant "lexi_pregnant" if_all ["lexi", "lexi_pregnant"] if_not ["bottomless", "naked"]
        group top auto variant "lexi_pregnant" if_all ["lexi", "lexi_pregnant"] if_not ["topless", "naked"]

        group lexi_eyes:
            attribute lexiopen default null
            attribute lexiclose null
        group exp_lexi auto variant "lexiopen" if_all ["lexi", "lexiopen"]:
            attribute lexinormal default
        group exp_lexi auto variant "lexiclose" if_all ["lexi", "lexiclose"]


        attribute breemc
        attribute mc_pubes if_any ["breemc"]
        attribute mc_collar if_any ["breemc"]
        attribute mc_pregnant if_any ["breemc"]
        group multiple auto variant piercings_breemc when breemc
        group bot auto variant "breemc" if_any ["breemc"] if_not ["mc_pregnant", "bottomless", "naked"]
        group top auto variant "breemc" if_any ["breemc"] if_not ["mc_pregnant", "topless", "naked"]
        group bot auto variant "breemc_pregnant" if_all ["breemc", "mc_pregnant"] if_not ["bottomless", "naked"]
        group top auto variant "breemc_pregnant" if_all ["breemc", "mc_pregnant"] if_not ["topless", "naked"]


        attribute bree
        attribute bree_pubes if_any ["bree"]
        attribute bree_collar if_any ["bree"]
        attribute bree_pregnant if_any ["bree"]
        group bot auto variant "bree" if_any ["bree"] if_not ["bree_pregnant", "bottomless", "naked"]
        group top auto variant "bree" if_any ["bree"] if_not ["bree_pregnant", "topless", "naked"]
        group bot auto variant "bree_pregnant" if_all ["bree", "bree_pregnant"] if_not ["bottomless", "naked"]
        group top auto variant "bree_pregnant" if_all ["bree", "bree_pregnant"] if_not ["topless", "naked"]
        group exp_bree auto if_any ["bree", "breemc"]:
            attribute breenormal default

        group joint auto if_not ["breesmoke", "lexismoke", "mikesmoke"]:
            attribute lexihold default

        group jointsmoke auto


        group multiple auto variant hairdetails

        group seasons:
            attribute spring null
            attribute summer null
            attribute fall null


        group multiple auto variant hairsnow when winter and parking


        attribute winter if_any ["parking"]

    layeredimage threesome breelexi breefuck:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker, CollarPicker], append_npc_from_attributes=True)

        group multiple:
            attribute bree_ears null
            attribute bree_lips null
            attribute bree_tongue null
            attribute lexi_clit null
            attribute lexi_navel null
            attribute lexi_pregnant_navel null
            attribute lexi_nipples null
            attribute lexi_tongue null

        group bg auto:
            attribute bedroom default

        attribute bree default

        group multiple auto variant pregnancy

        attribute bree_hand
        group multiple auto variant piercings_bree
        attribute bree_naked null
        group outfits_bree auto if_not "bree_naked"

        group exp_bree auto:
            attribute normal default

        attribute lexi

        group multiple auto variant collars
        group multiple auto variant piercings_lexi when lexi

        attribute lexi_naked null
        group outfits_lexi auto if_any "lexi" if_not "lexi_naked"

        always:
            if_not "squeeze"
            "threesome_breelexi_breefuck_balls"

        group dick_outside auto if_not ["vaginal", "anal"]
        group dick_inside auto if_any ["vaginal", "anal"]

        attribute cum null
        group dickcum auto if_any "cum"

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute condom null
        group condom_outside auto if_any "condom" if_not ["vaginal", "anal"]

        group condomcum auto if_all ["condom", "cum"] if_not ["vaginal", "anal"]

        attribute creampie

        group lexi_hand auto if_any "lexi":
            attribute fingering default

        attribute handjob null
        group handjob auto if_all ["lexi", "handjob"]

        group fg auto:
            attribute bedroom default

    layeredimage threesome breelexi lexifuck:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, DickPicker, OutfitPicker, CollarPicker], append_npc_from_attributes=True)

        group bg auto:
            attribute bedroom default

        attribute bree

        attribute lexi default

        group multiple auto variant pregnancy

        attribute mike

        group multiple auto variant piercings_lexi

        group multiple auto variant piercings_bree when bree

        group exp_lexi auto:
            attribute lexinormal default

        group exp_bree auto if_any "bree":
            attribute breepleasure default

        group tongue auto

        group multiple auto variant collars

        group dick_outside auto if_not ["vaginal", "anal"] if_all "mike"
        group dick_inside auto if_any ["vaginal", "anal"] if_all "mike"

        attribute cum null
        group dickcum auto if_all ["cum", "mike"]

        attribute cumshot null
        group cumshot auto if_all ["cumshot", "mike"]

        attribute creampie null
        group creampie auto if_all ["creampie", "mike"]

        attribute condom null
        group condom_outside auto if_all ["condom", "mike"] if_not ["vaginal", "anal"]
        group condom_inside auto if_all ["condom", "mike", "vaginal"]

        group condomcum auto if_all ["condom", "cum", "mike"] if_not ["vaginal", "anal"]

        group fg auto:
            attribute bedroom default

    layeredimage threesome breeminami:
        attribute_function MultiPickers([HaircutPicker, PiercingsPicker, PregnancyPicker, DickPicker], npcs=[bree, minami])


        always:
            "threesome_breeminami_bg"


        always:
            "threesome_breeminami_bodies"


        group multiple auto variant preg



        group exp_bree auto:
            attribute breenormal default

        group exp_minami auto:
            attribute minaminormal default


        group tongue auto:
            attribute breetonguedown default


        attribute minami_nohaircut
        attribute minami_haircut


        group mouth auto:
            attribute minamibreathing default


        always:
            "threesome_breeminami_light"


        attribute mike


        group dick_out auto if_all ["out", "mike"]
        group dick auto:
            attribute out null default


        attribute creampie null
        group creampie auto if_all ["mike", "creampie"] if_not ["condom", "out"]


        attribute dickcum null
        group dickcum auto if_all ["mike", "out", "dickcum"] if_not ["condom"]


        attribute cumshot null
        group cumshot auto if_all ["mike", "out", "cumshot"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"] if_not ["out"]
        group condom auto variant "out" if_all ["mike", "out", "condom"] if_not ["cumshot"]


        group condomcum auto if_all ["mike", "out", "cumshot", "condom"]


        group multiple auto variant piercings

    layeredimage threesome breesasha:
        attribute_function MultiPickers([CollarPicker, PregnancyPicker, HaircutPicker], npcs=[bree, sasha])


        group bg auto:
            attribute bedroom default


        always:
            "threesome_breesasha_bodies"


        group collars auto


        attribute bree_nohaircut null
        attribute bree_haircut
        attribute sasha_haircut null
        attribute sasha_nohaircut


        group pregnancy auto


        attribute sasha_noboobjob null
        attribute sasha_boobjob



        group exp_bree auto:
            attribute breenormal default
            attribute breepleasure
            attribute breeahegao

        group exp_sasha auto:
            attribute sashanormal default
            attribute sashapleasure
            attribute sashaahegao


        group multiple auto variant piercings


        attribute cum null
        group multiple auto variant cum when cum 


        attribute slapedbree
        attribute slapedsasha



        group righthand auto:
            attribute squeezesasha
            attribute slapsasha


        group left_hand auto:
            attribute fingers null
            attribute dildo null

        group lefthand auto variant "fingers" if_any ["fingers"] if_not ["leash"]:
            attribute outfing default
            attribute vaginalfing
            attribute analfing

        group lefthand auto variant "dildo" if_any ["dildo"] if_not ["leash"]:
            attribute vaginaldild default
            attribute analdild


        attribute dripbree



        group lefthand auto if_not ["leash", "fingers", "dildo"]:
            attribute squeezebree
            attribute slapbree


        group dick auto


        attribute condom null
        group condom auto if_any ["condom"]


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute dripsasha


        group dick_out auto if_not ["vaginaltip", "vaginal", "anal"]:
            attribute onsasha default
            attribute onbree


        group condom_out auto if_any ["condom"] if_not ["vaginaltip", "vaginal", "anal", "cumshot"]


        group condomcum auto if_all ["condom", "cumshot"] if_not ["vaginaltip", "vaginal", "anal"]


        attribute fap null
        group righthand auto variant "fap_onsasha" if_all ["fap", "onsasha"] if_not ["vaginaltip", "vaginal", "anal", "squeezesasha", "slapsasha"]:
            attribute sashafap default
        group righthand auto variant "fap_onbree" if_all ["fap", "onbree"] if_not ["vaginaltip", "vaginal", "anal", "squeezesasha", "slapsasha"]:
            attribute breefap default


        attribute fx null
        group fx auto variant "fap_onsasha" if_all ["fx", "onsasha"] if_not ["vaginaltip", "vaginal", "anal"]
        group fx auto variant "fap_onbree" if_all ["fx", "onbree"] if_not ["vaginaltip", "vaginal", "anal"]


        attribute cumshot null
        group cumshot auto if_any ["cumshot"] if_not ["vaginaltip", "vaginal", "anal", "condom"]


        group lefthand auto if_any ["bree_collar", "sasha_collar"]:
            attribute leash


        attribute sashaleash default if_all ["leash", "sasha_collar"]
        attribute breeleash default if_all ["leash", "bree_collar"]

    layeredimage threesome minamisasha :
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, DickPicker], npcs=[minami], append_npc_from_attributes=True)


        always:
            "threesome_minamisasha_bg"


        attribute minami


        group multiple auto variant piercings_minami


        group exp_minami auto:
            attribute minaminormal default


        group minamihair auto


        attribute minami_pregnant


        attribute mike null
        group mike if_all ["mike"]:
            attribute fuckminami default


        attribute licksasha if_all ["mike", "fuckminami"]


        attribute sasha


        group multiple auto variant piercings_sasha when sasha
        group multiple auto variant piercings_sasha_noboobjob when sasha and not sasha_boobjob


        attribute sasha_pregnant if_any ["sasha"]


        attribute sasha_boobjob if_any ["sasha"]


        group sashahair auto if_any ["sasha"]


        group exp_sasha auto if_any ["sasha"]:
            attribute sashanormal default


        group mike if_all ["mike"]:
            attribute fucksasha if_any ["sasha"]


        group fuck:
            attribute out null default
            attribute vaginal null
            attribute anal null


        group dick_out auto variant "fuckminami" if_all ["mike", "out", "fuckminami"]
        group dick_out auto variant "fucksasha" if_all ["mike", "out", "sasha", "fucksasha"]
        group dick auto variant "fuckminami" if_all ["mike", "fuckminami"]
        group dick auto variant "fucksasha" if_all ["mike", "sasha", "fucksasha"]


        attribute creampie null
        group creampie auto variant "fuckminami" if_all ["mike", "fuckminami", "creampie"] if_not ["condom"]
        group creampie auto variant "fucksasha" if_all ["mike", "sasha", "fucksasha", "creampie"] if_not ["condom"]


        attribute condom null
        group condom_out auto variant "fuckminami" if_all ["mike", "out", "fuckminami", "condom"] if_not ["cumshot"]
        group condom_out auto variant "fucksasha" if_all ["mike", "out", "sasha", "fucksasha", "condom"] if_not ["cumshot"]
        group condom auto variant "fuckminami" if_all ["mike", "fuckminami", "condom"]
        group condom auto variant "fucksasha" if_all ["mike", "sasha", "fucksasha", "condom"]


        group condomcum auto variant "fuckminami" if_all ["mike", "out", "fuckminami", "condom", "cumshot"]
        group condomcum auto variant "fucksasha" if_all ["mike", "out", "sasha", "fucksasha", "condom", "cumshot"]


        attribute cumshot null
        group cumshot auto variant "fuckminami" if_all ["mike", "out", "fuckminami", "cumshot"] if_not ["condom"]
        group cumshot auto variant "fucksasha" if_all ["mike", "out", "sasha", "fucksasha", "cumshot"] if_not ["condom"]

    layeredimage xmas diner:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker], append_npc_from_attributes=True)


        always "xmas_diner_bg"

        attribute mc_naked null
        attribute mc_casual default null
        attribute mc_pubes null


        attribute mike

        group mike_dick auto:
            attribute mike_big null
            attribute mike_medium null
            attribute mike_small null

        group mike_haircuts auto:
            attribute mike_haircut null
            attribute mike_nohaircut null


        group mike_outfits:
            attribute mike_casual default null
            attribute mike_naked null
        group mike_outfit auto if_any ["mike"]


        always "xmas_diner_mike_arms" if_any ["mike"]


        group mike_outfit_arm auto if_any ["mike"]


        group mike_exp auto if_any ["mike"]:
            attribute mike_yummy default


        attribute mikemc

        group mikemc_dicks auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group mikemc_outfit auto if_any ["mikemc"] if_not ["mc_naked"]


        always "xmas_diner_mikemc_arms" if_any ["mikemc"]


        group mikemc_outfit_arm auto if_any ["mikemc"] if_not ["mc_naked"]


        group mikemc_exp auto if_any ["mikemc"]:
            attribute mikemc_yummy default


        attribute bree


        attribute bree_pregnant if_any ["bree"]


        group bree_exp auto if_any ["bree"]:
            attribute bree_yummy default


        group multiple auto variant bree_piercings when bree
        group multiple:
            attribute bree_clit null
            attribute bree_tongue null


        group bree_outfits:
            attribute bree_casual default null
            attribute bree_naked null
        group bree_outfit auto if_any ["bree"]
        group bree_outfit auto variant "pregnant" if_all ["bree", "bree_pregnant"]


        attribute bree_collar if_any ["bree"]


        attribute breemc

        attribute mc_haircut if_any ["breemc"]
        attribute mc_nohaircut null if_any ["breemc"]


        attribute mc_pregnant if_any ["breemc"]


        group breemc_exp auto if_any ["breemc"]:
            attribute breemc_yummy default


        group multiple auto variant breemc_piercings when breemc


        group breemc_outfit auto if_any ["breemc"] if_not ["mc_naked"]
        group breemc_outfit auto variant "pregnant" if_all ["breemc", "mc_pregnant"] if_not ["mc_naked"]


        attribute mc_collar if_any ["breemc"]



        attribute sasha


        attribute sasha_pregnant if_any ["sasha"]


        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        group sasha_boobjob if_all ["sasha", "sasha_boobjob"]:
            attribute sasha_naked


        group sasha_exp auto if_any ["sasha"]:
            attribute sasha_yummy default


        group multiple auto variant sasha_piercings when sasha
        group multiple:
            attribute sasha_clit null
            attribute sasha_lips null
            attribute sasha_navel null
        group multiple auto variant sasha_piercings_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_notbb when sasha and not sasha_boobjob
        group multiple auto variant sasha_piercings_sasha_disgust when sasha and sasha_disgust


        group sasha_outfits:
            attribute sasha_casual default null
            attribute sasha_naked null
        group sasha_outfit auto if_any ["sasha"]
        group sasha_outfit auto variant "pregnant" if_all ["sasha", "sasha_pregnant"]


        group sasha_boobjob if_all ["sasha", "sasha_boobjob"]:
            attribute sasha_casual


        attribute sasha_collar if_any ["sasha"]


        attribute sasha_haircut if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]


        group multiple auto variant sasha_piercings_ears when sasha and sasha_ears


        attribute samantha

        attribute samantha_nohaircut null

        attribute samantha_pregnant if_any ["samantha"]


        group samantha_exp auto if_any ["samantha"]:
            attribute samantha_yummy default


        group multiple auto variant samantha_piercings when samantha
        group multiple:
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_tongue null


        group samantha_outfits:
            attribute samantha_casual default null
            attribute samantha_naked null
        group samantha_outfit auto if_any ["samantha"]


        always "xmas_diner_samantha_arms" if_any ["samantha"]


        group samantha_outfit auto variant "pregnant" if_all ["samantha", "samantha_pregnant"]


        attribute samantha_collar if_any ["samantha"]


        attribute lexi

        attribute lexi_nohaircut null


        attribute lexi_pregnant if_any ["lexi"]


        group lexi_exp auto if_any ["lexi"]:
            attribute lexi_yummy default


        group multiple auto variant lexi_piercings when lexi
        group multiple:
            attribute lexi_clit null
            attribute lexi_tongue null


        group lexi_outfits:
            attribute lexi_casual default null
            attribute lexi_naked null
        group lexi_outfit auto if_any ["lexi"]


        always "xmas_diner_lexi_arms" if_any ["lexi"]


        group lexi_outfit auto variant "pregnant" if_all ["lexi", "lexi_pregnant"]


        attribute lexi_collar if_any ["lexi"]


        attribute minami


        attribute minami_pregnant if_any ["minami"]


        group minami_exp auto if_any ["minami"]:
            attribute minami_yummy default


        group multiple auto variant minami_piercings when minami
        group multiple:
            attribute minami_nose null
            attribute minami_ears null


        group minami_outfits:
            attribute minami_casual default null
            attribute minami_naked null
        group minami_outfit auto if_any ["minami"]


        always "xmas_diner_minami_arms" if_any ["minami"]


        group minami_outfit_arm auto if_any ["minami"]


        group minami_outfit auto variant "pregnant" if_all ["minami", "minami_pregnant"]


        attribute minami_collar if_any ["minami"]


        attribute minami_haircut if_any ["minami"]
        attribute minami_nohaircut if_any ["minami"]


        always "xmas_diner_table"


        group multiple auto variant eat

        group meal:
            attribute goodmeal default null
            attribute badmeal null


        group multiple auto variant goodmeal when goodmeal
        group multiple auto variant badmeal when badmeal


        always "xmas_diner_mashed_potato"
        always "xmas_diner_turkey_plate"
        always "xmas_diner_goodturkey" if_any ["goodmeal"]
        always "xmas_diner_badturkey" if_any ["badmeal"]
        always "xmas_diner_turkey_spices"

    layeredimage xmas singing:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker], append_npc_from_attributes=True)

        attribute mc_casual default null
        attribute mc_naked null
        attribute mc_pubes null


        group singer:
            attribute singmikemc default null
            attribute singbreemc null
            attribute singminami null


        always "xmas_singing_bg"


        attribute bree


        attribute bree_pregnant null
        group bree_outfit:
            attribute bree_casual default null
            attribute bree_naked null
        group bree_outfit auto if_any ["bree"]


        group bree_exp auto if_any ["bree"]:
            attribute bree_happy default


        group bree_outfit_arm auto variant "bree_happy" if_all ["bree", "bree_happy"]


        attribute bree_collar if_any ["bree"]


        group multiple auto variant bree_piercings when bree
        group multiple:
            attribute bree_clit null
            attribute bree_navel null
            attribute bree_pregnant_navel null
            attribute bree_nipples null
            attribute bree_tongue null

        group bree_outfit_arm auto variant "bree_annoyed" if_all ["bree", "bree_annoyed"]


        attribute breemc if_not ["singbreemc"]

        attribute mc_pregnant null if_not ["singbreemc"]


        group breemc_outfit auto if_any ["breemc"] if_not ["singbreemc"]


        group breemc_exp auto if_any ["breemc"] if_not ["singbreemc"]:
            attribute breemc_happy default


        group breemc_outfit_arm auto variant "breemc_happy" if_all ["breemc", "breemc_happy"] if_not ["singbreemc"]
        group breemc_outfit_arm auto variant "breemc_annoyed" if_all ["breemc", "breemc_annoyed"] if_not ["singbreemc"]


        attribute mc_collar if_any ["breemc"] if_not ["singbreemc"]


        group multiple auto variant breemc_piercings when breemc and not singbreemc


        attribute lexi

        attribute lexi_nohaircut null

        attribute lexi_pregnant if_any ["lexi"]


        group multiple auto variant lexi_piercings when lexi
        group multiple:
            attribute lexi_tongue null


        group lexi_outfits:
            attribute lexi_casual default null
            attribute lexi_naked null
        group lexi_outfit auto if_any ["lexi"]
        group lexi_outfit auto variant "pregnant" if_all ["lexi", "lexi_pregnant"]


        group lexi_exp auto if_any ["lexi"]:
            attribute lexi_happy default


        attribute lexi_collar if_any ["lexi"]




        attribute samantha

        attribute samantha_nohaircut null

        attribute samantha_pregnant if_any ["samantha"]


        group multiple auto variant samantha_piercings when samantha
        group multiple:
            attribute samantha_ears null
            attribute samantha_nose null
            attribute samantha_tongue null


        group samantha_outfits:
            attribute samantha_casual default null
            attribute samantha_naked null

        group samantha_outfit auto if_any ["samantha"]
        group samantha_outfit auto variant "pregnant" if_all ["samantha", "samantha_pregnant"]


        group samantha_exp auto if_any ["samantha"]:
            attribute samantha_happy default

        group multiple auto variant samantha_piercings_samantha_happy when samantha and samantha_happy
        group multiple auto variant samantha_piercings_samantha_annoyed when samantha and samantha_annoyed


        attribute samantha_collar if_any ["samantha"]




        attribute sasha


        attribute sasha_pregnant if_any ["sasha"]


        group sasha_outfits:
            attribute sasha_casual default null
            attribute sasha_naked null
        group sasha_outfit auto if_any ["sasha"]


        attribute sasha_haircut if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]


        group multiple auto variant sasha_piercings_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_notbb when sasha and not sasha_boobjob
        group multiple auto variant sasha_piercings when sasha
        group multiple:
            attribute sasha_lips null

        group sasha_outfit auto variant "pregnant" if_all ["sasha", "sasha_pregnant"]


        group sasha_exp auto if_any ["sasha"]:
            attribute sasha_happy default


        group sasha_outfit_arm auto variant "sasha_happy" if_all ["sasha", "sasha_happy"]

        group sasha_outfit_arm auto variant "sasha_annoyed" if_all ["sasha", "sasha_annoyed"]


        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        group sasha_boobjob auto if_all ["sasha", "sasha_boobjob"]


        attribute sasha_collar if_any ["sasha"]


        attribute minami if_not ["singminami"]


        attribute minami_pregnant if_any ["minami"] if_not ["singminami"]


        group multiple auto variant minami_piercings when minami and not singminami
        group multiple:
            attribute minami_ears null


        group minami_outfits:
            attribute minami_casual default null
            attribute minami_naked null
        group minami_outfit auto if_any ["minami"] if_not ["singminami"]


        attribute minami_collar if_any ["minami"] if_not ["singminami"]


        group minami_haircuts auto if_any ["minami"] if_not ["singminami"]



        group minami_outfit auto variant "pregnant" if_all ["minami", "minami_pregnant"] if_not ["singminami"]


        group minami_exp auto if_any ["minami"] if_not ["singminami"]:
            attribute minami_happy default


        group minami_outfit_arm auto variant "minami_happy" if_all ["minami", "minami_happy"] if_not ["singminami"]
        group minami_outfit_arm auto variant "minami_annoyed" if_all ["minami", "minami_annoyed"] if_not ["singminami"]


        attribute mike if_not ["singmike"]

        group mike_dick auto:
            attribute mike_big null
            attribute mike_medium null
            attribute mike_small null

        group mike_haircuts auto:
            attribute mike_haircut null
            attribute mike_nohaircut null


        attribute mike_casual default null
        group mike_outfit auto if_not ["singmike"] if_any "mike"


        group mike_exp auto if_not ["singmike"] if_any "mike":
            attribute mike_happy default


        group mike_outfit_arm auto variant "mike_happy" if_all ["mike_happy", "mike"] if_not ["singmike"]
        group mike_outfit_arm auto variant "mike_annoyed" if_all ["mike_annoyed", "mike"] if_not ["singmike"]


        attribute mikemc if_not ["singmikemc"]

        group mikemc_dick auto:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group mikemc_outfit auto if_any "mikemc" if_not ["singmikemc"]


        group mikemc_exp auto if_any "mikemc" if_not ["singmikemc"]:
            attribute mikemc_happy default


        group mikemc_outfit_arm auto variant "mikemc_happy" if_all ["mikemc", "mikemc_happy"] if_not ["singmikemc"]
        group mikemc_outfit_arm auto variant "mikemc_annoyed" if_all ["mikemc", "mikemc_annoyed"] if_not ["singmikemc"]


        attribute singminami

        always "xmas_singing_singminami_pregnant" if_all ["singminami", "minami_pregnant"]


        group multiple auto variant singminami_piercings when singminami


        group singminami_outfit auto if_any ["singminami"]
        group singminami_outfit auto variant "pregnant" if_all ["singminami", "minami_pregnant"]


        group singminami_collar auto if_any ["singminami"]


        group singminami_haircuts auto if_any ["singminami"]


        attribute singmike


        group singmike_outfit auto if_any ["singmike"]


        attribute singmikemc


        group singmikemc_outfit auto if_any ["singmikemc"]


        attribute singbreemc

        always "xmas_singing_singbreemc_mc_pregnant" if_all ["singbreemc", "mc_pregnant"]


        group multiple auto variant singbreemc_piercings when singbreemc


        group singbreemc_outfit auto if_any ["singbreemc"]
        group singbreemc_outfit auto variant "pregnant" if_all ["singbreemc", "mc_pregnant"]


        group singbreemc_collar auto if_any ["singbreemc"]


        group singbreemc_haircuts auto if_any ["singbreemc"]:
            attribute mc_nohaircut null



        group light auto


    layeredimage xmas snacks:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, CollarPicker, OutfitPicker, MCCGPicker], append_npc_from_attributes=True)


        always "xmas_snacks_bg"

        attribute mc_naked null
        attribute mc_casual default null
        attribute mc_pubes null


        attribute mike

        group mike_dick auto:
            attribute mike_big null
            attribute mike_medium null
            attribute mike_small null

        group mike_haircuts auto:
            attribute mike_haircut null
            attribute mike_nohaircut null


        group mike_exp auto if_any ["mike"]:
            attribute mike_yummy default


        attribute mike_naked null
        attribute mike_casual default null
        group mike_outfit auto if_any ["mike"] if_not ["mike_naked"]


        attribute mikemc

        group mc_dick:
            attribute mc_big null
            attribute mc_medium null
            attribute mc_small null


        group mikemc_exp auto if_any ["mikemc"]:
            attribute mikemc_yummy default


        group mikemc_outfit auto if_any ["mikemc"] if_not ["mc_naked"]


        attribute minami


        attribute minami_pregnant if_all ["minami", "minami_naked"]


        group minami_exp auto if_any ["minami"]:
            attribute minami_yummy default


        group multiple auto variant minami_piercings_under when minami
        group multiple:
            attribute minami_clit null
            attribute minami_ears null


        attribute minami_naked null
        attribute minami_casual default null
        group minami_outfit auto if_any ["minami"] if_not ["minami_naked"]
        group minami_outfit auto variant "pregnant" if_all ["minami", "minami_pregnant"] if_not ["minami_naked"]


        attribute minami_collar if_any ["minami"]


        attribute minami_haircut if_any ["minami"]
        attribute minami_nohaircut if_any ["minami"]


        group multiple auto variant minami_piercings when minami


        attribute sasha


        attribute sasha_pregnant if_all ["sasha", "sasha_naked"]


        attribute sasha_boobjob if_all ["sasha", "sasha_naked"]
        attribute sasha_noboobjob null


        group sasha_exp auto if_any ["sasha"]:
            attribute sasha_yummy default


        group multiple auto variant sasha_piercings_under when sasha
        group multiple:
            attribute sasha_clit null
            attribute sasha_lips null
            attribute sasha_tongue null
        group multiple auto variant sasha_piercings_under_bb when sasha and sasha_boobjob
        group multiple auto variant sasha_piercings_under_notbb when sasha and not sasha_boobjob


        attribute sasha_naked null
        attribute sasha_casual default null
        group sasha_outfit auto if_any ["sasha"] if_not ["sasha_naked"]
        group sasha_outfit auto variant "pregnant" if_all ["sasha", "sasha_pregnant"] if_not ["sasha_naked"]
        group sasha_outfit auto variant "boobjob" if_all ["sasha", "sasha_boobjob"] if_not ["sasha_naked"]


        attribute sasha_collar if_any ["sasha"]


        attribute sasha_haircut if_any ["sasha"]
        attribute sasha_nohaircut if_any ["sasha"]


        group multiple auto variant sasha_piercings when sasha


        attribute samantha

        attribute samantha_haircut null
        attribute samantha_nohaircut null


        attribute samantha_pregnant if_all ["samantha", "samantha_naked"]


        group samantha_exp auto if_any ["samantha"]:
            attribute samantha_yummy default


        group multiple auto variant samantha_piercings_under when samantha
        group multiple:
            attribute samantha_ears null
            attribute samantha_clit null
            attribute samantha_tongue null


        attribute samantha_naked null
        attribute samantha_casual default null
        group samantha_outfit auto if_any ["samantha"] if_not ["samantha_naked"]
        group samantha_outfit auto variant "pregnant" if_all ["samantha", "samantha_pregnant"] if_not ["samantha_naked"]


        attribute samantha_collar if_any ["samantha"]


        group multiple auto variant samantha_piercings when samantha


        attribute lexi

        attribute lexi_haircut null
        attribute lexi_nohaircut null


        attribute lexi_pregnant if_all ["lexi", "lexi_naked"]


        group lexi_exp auto if_any ["lexi"]:
            attribute lexi_yummy default


        group multiple auto variant lexi_piercings_under when lexi
        group multiple:
            attribute lexi_clit null
            attribute lexi_tongue null


        attribute lexi_naked null
        attribute lexi_casual default null
        group lexi_outfit auto if_any ["lexi"] if_not ["lexi_naked"]
        group lexi_outfit auto variant "pregnant" if_all ["lexi", "lexi_pregnant"] if_not ["lexi_naked"]


        attribute lexi_collar


        group multiple auto variant lexi_piercings when lexi


        attribute bree

        attribute bree_haircut null
        attribute bree_nohaircut null


        attribute bree_pregnant if_all ["bree", "bree_naked"]


        group bree_exp auto if_any ["bree"]:
            attribute bree_yummy default


        group multiple auto variant bree_piercings when bree
        group multiple:
            attribute bree_clit null
            attribute bree_ears null
            attribute bree_nose null
            attribute bree_tongue null


        attribute bree_naked null
        attribute bree_casual default null
        group bree_outfit auto if_any ["bree"] if_not ["bree_naked"]
        group bree_outfit auto variant "pregnant" if_all ["bree", "bree_pregnant"] if_not ["bree_naked"]


        attribute bree_collar if_any ["bree"]


        attribute breemc

        attribute mc_haircut if_any ["breemc"]
        attribute mc_nohaircut null if_any ["breemc"]


        attribute mc_pregnant if_all ["breemc", "mc_naked"]


        group breemc_exp auto if_any ["breemc"]:
            attribute breemc_yummy default


        group multiple auto variant breemc_piercings when breemc
        group multiple:
            attribute mc_ears null


        group breemc_outfit auto if_any ["breemc"] if_not ["mc_naked"]
        group breemc_outfit auto variant "pregnant" if_all ["breemc", "mc_pregnant"] if_not ["mc_naked"]


        attribute mc_collar if_any ["breemc"]


        always "xmas_snacks_table"
        always "xmas_snacks_armcouch"


        group food auto:
            attribute homemade default


    layeredimage threesome samsasha samfuck:
        attribute_function MultiPickers([PiercingsPicker, PregnancyPicker, HaircutPicker, OutfitPicker, CollarPicker, RoomPicker], append_npc_from_attributes=True)

        attribute naked null
        attribute samantha_naked null
        attribute sasha_naked null
        attribute samantha_haircut null
        attribute samantha_nohaircut null
        attribute samantha_collar null

        group bg auto:
            attribute bedroom default

        attribute nomc null
        group mikemc auto if_not "nomc":
            attribute left default

        attribute samantha default
        attribute samantha_pregnant

        group mikemc_hands auto if_not "nomc"

        group multiple auto variant piercings_samantha
        group multiple:
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_navel null
            attribute samantha_pregnant_navel null
            attribute samantha_tongue null

        group outfits_samantha_back auto if_not "samantha_naked"

        attribute sasha

        attribute sasha_pregnant
        attribute sasha_boobjob if_any "sasha"
        attribute sasha_nohaircut if_any "sasha"
        attribute sasha_haircut null

        group multiple auto variant piercings_sasha when sasha
        group multiple:
            attribute sasha_clit null
            attribute sasha_nose null
            attribute sasha_lips null
            attribute sasha_navel null
            attribute sasha_pregnant_navel null
            attribute sasha_tongue null

        group piercings_sasha auto variant "boobjob" if_all ["sasha", "sasha_boobjob"]
        group piercings_sasha auto variant "noboobjob" if_all ["sasha"] if_not ["sasha_boobjob"]

        group outfits_samantha_front auto if_not "samantha_naked"

        group outfits_sasha_bot auto if_any "sasha" if_not "sasha_naked"
        group outfits_sasha_top auto variant "boobjob" if_all ["sasha", "sasha_boobjob"] if_not "sasha_naked"
        group outfits_sasha_top auto variant "noboobjob" if_all ["sasha"] if_not ["sasha_boobjob", "sasha_naked"]
        attribute sasha_collar

        always:
            if_not "sasha"
            "threesome_samsasha_samfuck_samantha_hands"

        group multiple auto variant piercings_samantha when not sasha:
            attribute samantha_clit null
            attribute samantha_ears null
            attribute samantha_lips null
            attribute samantha_navel null
            attribute samantha_pregnant_navel null
            attribute samantha_tongue null

        group outfits_samantha_hands auto if_not ["samantha_naked", "sasha"]

        group exp_sam auto:
            attribute samnormal default

        attribute tongue

        group fg auto

    layeredimage threesome samsasha sashafuck:
        attribute_function MultiPickers([PubesPicker, PiercingsPicker, PregnancyPicker, HaircutPicker, OutfitPicker, CollarPicker, DickPicker, RoomPicker], append_npc_from_attributes=True)

        attribute naked null
        attribute samantha_naked null
        attribute samantha_haircut null
        attribute samantha_nohaircut null
        attribute sasha_naked null

        group bg auto:
            attribute bedroom default

        attribute sasha default null

        attribute samantha null
        attribute samantha_pregnant null
        attribute samantha_pubes null

        always:
            if_any "samantha"
            "threesome_samsasha_sashafuck_samantha_lower"

        group outfits_samantha_bot auto if_any "samantha" if_not "samantha_naked"

        always:
            "threesome_samsasha_sashafuck_mikemc"

        group body auto:
            attribute up default

        attribute sasha_collar

        group boobs auto

        group multiple auto variant piercings_sasha_up when up
        group multiple auto variant piercings_sasha_down when down
        group piercings_sasha auto variant "boobjob" if_any "sasha_boobjob"
        group piercings_sasha auto variant "noboobjob" if_any "sasha_noboobjob"

        group outfits_sasha auto variant "boobjob" if_any "sasha_boobjob"
        group outfits_sasha auto variant "noboobjob" if_any "sasha_noboobjob"

        attribute sasha_pregnant null
        group sasha_pregnant auto if_any "sasha_pregnant"

        group multiple auto variant piercings_sasha
        group multiple:
            attribute sasha_lips null
            attribute sasha_tongue null

        group pubes auto variant "up" if_all ["up", "sasha_pubes"]
        group pubes auto variant "down" if_all ["down", "sasha_pubes"]

        attribute cum null
        attribute condom null
        group cum auto if_any "cum" if_not "condom"

        group haircuts_straight auto if_not "samantha"
        group multiple auto variant piercings_sasha_straight when not samantha
        group mouth_straight auto if_not "samantha":
            attribute sasha_normal default
        group eyes_straight auto if_not "samantha":
            attribute sasha_opened default

        group samantha_upper auto if_any "samantha"
        group outfits_samantha_top variant "up" auto if_all ["samantha", "up"] if_not "samantha_naked"
        group outfits_samantha_top variant "down" auto if_all ["samantha", "down"] if_not "samantha_naked"

        group haircuts_left auto if_any "samantha":
            attribute sasha_haircut null

        group multiple auto variant piercings_sasha_left when samantha

        attribute samantha_collar

        group eyes_left auto if_any "samantha":
            attribute sasha_opened default
        group eyes_samantha auto if_any "samantha":
            attribute samantha_opened default

        group multiple auto variant piercings_samantha
        group multiple:
            attribute samantha_clit null
            attribute samantha_navel null
            attribute samantha_pregnant_navel null
            attribute samantha_lips null
            attribute samantha_nipples null
            attribute samantha_tongue null
            attribute samantha_ears null

        group samantha_arm auto variant "up" if_all ["samantha", "up"]:
            attribute face default
        group samantha_arm auto variant "down" if_all ["samantha", "down"]

        group dick_location:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto variant "vaginal" if_any "vaginal"
        group dick auto variant "anal" if_any "anal"

        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto variant "vaginal" if_all ["vaginal", "condom"]
        group condom auto variant "anal" if_all ["anal", "condom"]

        attribute cumshot null
        group cumshot auto if_any "cumshot" if_not "condom"
        group condomcum auto if_all ["cumshot", "condom"]

        attribute creampie null
        group creampie auto if_not "out" if_any "creampie"

        attribute squirt null
        group squirt auto if_all ["samantha", "squirt"]


        group fg auto

    layeredimage sunscreen bree sasha:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, OutfitPicker, HaircutPicker, PiercingsPicker], npcs=[bree, sasha])

        attribute naked null
        attribute topless null
        attribute bree_topless null
        attribute sasha_topless null

        group multiple:
            attribute bree_clit null
            attribute bree_collar null
            attribute bree_ears null
            attribute bree_navel null
            attribute bree_pregnant_navel null
            attribute bree_tongue null
            attribute sasha_lips null
            attribute sasha_tongue null

        always "sunscreen_bree_sasha_bg_pool"

        attribute nosasha null
        attribute sasha when not nosasha
        attribute sasha_pregnant when not nosasha
        attribute sasha_boobjob when not nosasha
        group haircuts auto when not nosasha

        group multiple auto variant sasha_piercings when not nosasha
        group sasha_piercings auto variant noboobjob when not sasha_boobjob and not nosasha
        group sasha_piercings auto variant boobjob when sasha_boobjob and not nosasha

        group sasha_bot auto when not (naked or nosasha or sasha_pregnant)
        group sasha_bot auto variant pregnant when sasha_pregnant and not (naked or nosasha)
        group sasha_top auto variant noboobjob when not sasha_boobjob and not (naked or topless or sasha_topless or nosasha)
        group sasha_top auto variant boobjob when sasha_boobjob and not (naked or topless or sasha_topless or nosasha)

        attribute sasha_collar when not nosasha

        attribute bree
        attribute bree_haircut
        attribute bree_nohaircut null
        attribute bree_pregnant null
        group multiple auto variant bree_piercings

        group bree_bot auto when not (naked)
        group bree_top auto when not (naked or topless or bree_topless)

        always "sunscreen_bree_sasha_bottle"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
