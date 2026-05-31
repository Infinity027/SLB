init 1:
    layeredimage goth 3some blowjob:
        attribute_function Pickers([PiercingsPicker, PregnancyPicker], npc=amy)




        always "goth_3some_blowjob_bg"


        attribute amyblow null
        attribute violaineblow null


        always "goth_3some_blowjob_mike_dualblow" if_all ["amyblow", "violaineblow"]



        group amybackarm auto
        always "goth_3some_blowjob_amybackarm_amylick" if_any ["violaineblow"] if_not ["amyblow"]

        attribute amytongue if_all ["amyblow", "violaineblow"]

        group amy auto
        always "goth_3some_blowjob_amy_amylick" if_any ["violaineblow"] if_not ["amyblow"]

        group pregnant auto if_any ["pregnant"]
        always "goth_3some_blowjob_pregnant_amylick" if_all ["pregnant", "violaineblow"] if_not ["amyblow"]

        group amyeyes auto variant "amyblow" if_any ["amyblow"]:
            attribute amyopen default
        group amyeyes auto variant "amylick" if_any ["violaineblow"] if_not ["amyblow"]:
            attribute amyopen default

        group multiple auto variant piercings_amyblow when amyblow
        group multiple auto variant piercings_amylick when violaineblow and not amyblow



        group violainebackarm auto
        always "goth_3some_blowjob_violainebackarm_violainelick" if_any ["amyblow"] if_not ["violaineblow"]

        attribute violainetongue if_all ["violaineblow", "amyblow"]

        group violaine auto
        always "goth_3some_blowjob_violaine_violainelick" if_any ["amyblow"] if_not ["violaineblow"]

        group violaineeyes auto variant "violaineblow" if_any ["violaineblow"]:
            attribute violaineopen default





        always "goth_3some_blowjob_mikehand_amy_dualblow" if_all ["amyblow", "violaineblow"]
        always "goth_3some_blowjob_amyhair" if_any ["amyblow"]
        always "goth_3some_blowjob_mikehand_amyblow" if_any ["amyblow"] if_not ["violaineblow"]

        always "goth_3some_blowjob_mikehand_violaine_dualblow" if_all ["violaineblow", "amyblow"]
        always "goth_3some_blowjob_mikehand_violaineblow" if_any ["violaineblow"] if_not ["amyblow"]


        attribute amyfacecum if_any ["amyblow"]
        attribute violainefacecum if_any ["violaineblow"]


        always "goth_3some_blowjob_mike_amyblow" if_any ["amyblow"] if_not["violaineblow"]
        always "goth_3some_blowjob_mike_violaineblow" if_any ["violaineblow"] if_not["amyblow"]

        group dick auto if_all ["amyblow", "violaineblow"]:
            attribute normal default

        attribute dickcum null
        group dickcum auto if_any ["dickcum"]



        group amyfrontarm auto
        always "goth_3some_blowjob_amyfrontarm_amylick" if_any ["violaineblow"] if_not ["amyblow"]

        group violainefrontarm auto
        always "goth_3some_blowjob_violainefrontarm_violainelick" if_any ["amyblow"] if_not ["violaineblow"]

    layeredimage goth 3some amyfuck:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, DickPicker], npc=amy)


        always "goth_3some_amyfuck_bg"


        always "goth_3some_amyfuck_violaine_righthand" if_any ["violaine", "bj"]


        always "goth_3some_amyfuck_amy"


        attribute collar
        attribute pubes


        attribute vaginaldrip


        group eyes auto:
            attribute eyesnormal default
        group mouth auto:
            attribute mouthnormal default


        attribute mike
        always "goth_3some_amyfuck_mikenormal" if_any ["mike"] if_not ["mikesuck"]
        attribute mikesuck if_any ["mike"]


        attribute pregnant


        group multiple auto variant piercings
        group multiple auto variant piercings_suck when suck
        group multiple auto variant piercings_nosuck when not mikesuck


        always "goth_3some_amyfuck_violaine_lefthand" if_any ["violaine"] if_not ["bj", "vaginal"]


        group dicks:
            attribute out default null
            attribute bj null
            attribute vaginal null
            attribute anal null
        group dick auto if_any ["mike"]
        group dick auto variant "out" if_all ["mike", "out"]


        attribute cum null
        group cum auto if_all ["mike", "cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["mike", "cum", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "condom", "out"] 



        always "goth_3some_amyfuck_violaine_lefthand" if_all ["violaine", "vaginal"] if_not ["bj"]
        attribute violaine if_not ["bj"]
        attribute bj if_any ["mike"]
        always "goth_3some_amyfuck_blowjobcum" if_all ["mike", "bj", "cum"] if_not ["condom"]

    layeredimage goth 3some violainefuck:
        attribute_function Pickers([DickPicker], npc=amy)


        always "goth_3some_violainefuck_bg"


        attribute amy
        always "goth_3some_violainefuck_violaine"


        attribute violaine_tongue null
        group viotongue auto if_any ["violaine_tongue"]


        group viohead auto:
            attribute headup default


        group vioeyes auto variant "headup" if_any ["headup"]:
            attribute violaine_eyesopen default
        group vioeyes auto variant "headdown" if_any ["headdown"]:
            attribute violaine_eyesopen default


        always "goth_3some_violainefuck_amyhead_normal" if_any ["amy"] if_not ["blowjob"]
        always "goth_3some_violainefuck_amyhead_blowjob" if_all ["amy", "blowjob"]


        group amyeyes auto variant "normal" if_any ["amy"] if_not ["blowjob"]:
            attribute amy_eyesopen default
        group amyeyes auto variant "blowjob" if_all ["amy", "blowjob"]:
            attribute amy_eyesopen default


        group dicks:
            attribute out default null
            attribute blowjob null
            attribute vaginal null
            attribute anal null
        group dick auto if_any ["mike"]
        group dick auto variant "out" if_all ["mike", "out"]


        attribute cum null
        group cum auto if_all ["mike", "cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["mike", "cum", "out"] if_not ["condom"]


        attribute condom null
        group condom auto if_all ["mike", "condom"]
        group condom auto variant "out" if_all ["mike", "condom", "out"] if_not ["cum"]
        group condomcum auto if_all ["mike", "condom", "cum", "out"]


        attribute mike null
        always "goth_3some_violainefuck_mike" if_any ["mike"] if_not ["blowjob"]
        always "goth_3some_violainefuck_mike_blowjob" if_all ["mike", "blowjob"]


        always "goth_3some_violainefuck_violaine_hand"
        always "goth_3some_violainefuck_mike_hand" if_any ["mike"]

    layeredimage goth 3some amydoubleblowjob:
        attribute_function Pickers([CollarPicker, PiercingsPicker], npc=amy)

        always "goth_3some_amydoubleblowjob_bg_room"
        always "goth_3some_amydoubleblowjob_amybody"

        group multiple auto variant piercings

        attribute collar

        group amyeyes auto:
            attribute eyes_open default

        group amymouth:
            attribute mouth_tongueout default
            attribute mouth_tongueup

        attribute tongueoutcum
        attribute cumface

        always "goth_3some_amydoubleblowjob_mikebody"

        group mikedick auto:
            attribute mikedown default

        attribute mikecum

        group amymouth:
            attribute mouth_mikebite
            attribute mouth_mikelips
            attribute mouth_mikesuck

        attribute mouthcum

        always "goth_3some_amydoubleblowjob_vincentbody"

        group vindick auto:
            attribute vindown default

        attribute vincum

        group amymouth:
            attribute mouth_vinbite
            attribute mouth_vinlips
            attribute mouth_vinsuck

        group amyhandleft auto if_all ["mikeup"]
        group amyhandright auto if_all ["vinup"]

        group amymouth:
            attribute mouth_doublebite
            attribute mouth_doublelips
            attribute mouth_doublesuck

        attribute doublebitecum
        attribute doublesuckcum

        group amyhandpose auto if_not ["leftnormal", "leftpull", "rightnormal", "rightpull"]

    layeredimage goth 3some amydoggy:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker, DickPicker, PubesPicker], npc=amy)


        always "goth_3some_amydoggy_bg"
        always "goth_3some_amydoggy_amy"


        attribute pubes
        attribute collar
        group multiple auto variant piercings
        attribute pregnant


        attribute vaginaldrip
        attribute bodycum
        attribute facecum


        group mouth auto if_not ["blowjob"]:
            attribute mouth_open default
        group eyes auto:
            attribute eyes_open default


        attribute vincent

        attribute blowjob if_any ["vincent"]
        always "goth_3some_amydoggy_vincent_dickout" if_any ["vincent"] if_not ["blowjob"]

        attribute vindickcum null
        always "goth_3some_amydoggy_vindickcum_blowjob" if_all ["vincent" ,"vindickcum", "blowjob"]
        always "goth_3some_amydoggy_vindickcum_dickout" if_all ["vincent", "vindickcum"] if_not ["blowjob"]

        attribute vincum null
        always "goth_3some_amydoggy_vincum_blowjob" if_all ["vincent", "vincum", "blowjob"]


        always "goth_3some_amydoggy_mike"
        group dick auto:
            attribute out null default
        group dick auto variant "out" if_any ["out"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["mikecum", "mikedickcum"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["mikecum", "mikedickcum"]
        group condomcum auto if_all ["condom", "out"] if_any ["mikecum", "mikedickcum"]


        attribute mikedickcum null
        group mikedickcum auto if_any ["mikedickcum"] if_not ["condom"]


        attribute mikecum null
        group mikecum auto if_any ["mikecum"] if_not ["condom"]
        group mikecum auto variant "out" if_all ["mikecum", "out"] if_not ["condom"]

    layeredimage goth 3some amyrevcow:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, DickPicker], npc=amy)


        always "goth_3some_amyrevcow_bg"
        always "goth_3some_amyrevcow_base"


        attribute wet
        attribute bodycum
        attribute facecum


        attribute pregnant
        group multiple auto variant piercings


        attribute vincent null
        group vincent auto if_any ["vincent"]:
            attribute walking default


        group dick auto if_all ["vincent", "onfloor"]:
            attribute out default


        attribute vincum null
        group vincum auto if_all ["vincent", "onfloor", "vincum"]


        attribute condom null
        group condom auto if_all ["vincent", "onfloor", "condom"] if_not["vincum"]
        group condomcum auto if_all ["vincent", "onfloor", "condom", "vincum"]


        group eyes auto:
            attribute eyes_open default
        group mouth auto if_not ["blowjob"]:
            attribute mouth_open default


        attribute blowjob
        group nobj auto if_not ["blowjob"]


        attribute mikecum null
        group mikecum auto if_any ["mikecum"]
        group mikecum auto variant "nobj" if_any ["mikecum"] if_not ["blowjob"]


        attribute handjob null
        group handjob auto if_any ["handjob"] if_not ["blowjob"]:
            attribute down default
        attribute speed if_any ["handjob"] if_not ["blowjob"]

    layeredimage goth 4some fuckamy:
        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker, DickPicker], npc=amy)


        always "goth_4some_fuckamy_bg"
        always "goth_4some_fuckamy_bodies"


        attribute amy_bodycum
        attribute violaine_bodycum


        group multiple auto variant piercings
        attribute pregnant
        attribute collar


        group amyeyes auto:
            attribute amyeyes_normal default
        group violaineeyes auto:
            attribute violaineeyes_normal default


        group vindick auto:
            attribute vinout default


        attribute vincum null
        group vincum auto if_any ["vincum"] if_not ["vincondom"]


        attribute vindoncom null
        group vindoncom if_any ["vindoncom"] if_not ["vincum"]:
            attribute vinout
        group vindoncom if_any ["vindoncom"]:
            attribute vinvaginal
        group vindoncomcum auto if_all ["vindoncom", "vincum"]


        always "goth_4some_fuckamy_mikebackhand"
        group mike auto:
            attribute back default


        always "goth_4some_fuckamy_mikedick_forth_mikevaginal" if_all ["forth", "mikeout"]
        group mikedick auto variant "forth" if_any ["forth"]:
            attribute mikeout null default 
        group mikedick auto variant "back" if_any ["back"]:
            attribute mikeout null default
        group mikedick auto variant "mikeout" if_all ["mikeout", "back"]


        attribute mikecum null
        group mikecum auto variant "back" if_all ["mikecum", "back"] if_not ["mikecondom"]
        group mikecum auto variant "mikeout" if_all ["mikecum", "mikeout", "back"] if_not ["mikecondom"]


        attribute mikecondom null
        group mikecondom auto variant "back" if_all ["mikecondom", "back"]
        group mikecondom auto variant "mikeout" if_all ["mikecondom", "mikeout", "back"] if_not ["mikecum"]
        group mikecondomcum auto variant "mikeout" if_all ["mikecondom", "mikecum", "mikeout", "back"]


        group mikehand auto:
            attribute onmike default

    layeredimage goth 4some fuckviolaine:
        attribute_function Pickers([PubesPicker, PregnancyPicker, CollarPicker, PiercingsPicker, DickPicker], npc=amy)


        always "goth_4some_fuckviolaine_bg"


        attribute amy


        attribute collar if_any ["amy"]
        attribute pubes if_any ["amy"]
        attribute pregnant if_any ["amy"]


        attribute amy_bodycum if_any ["amy"]


        always "goth_4some_fuckviolaine_boobs_normal" if_any ["amy"] if_not ["amybounce"]
        attribute amybounce null
        group boobs if_all ["amy", "amybounce"]:
            attribute bounce1 default
            attribute bounce2


        group multiple auto variant piercings when amy
        group multiple auto variant piercings_normal when amy and not amybounce
        group multiple auto variant piercings_bounce1 when amy and amybounce and bounce1
        group multiple auto variant piercings_bounce2 when amy and amybounce and bounce2


        attribute bouncespeed if_all ["amy", "amybounce"]


        group amymouths auto if_any ["amy"]:
            attribute amymouth_pleasure default
        group amyeyes auto if_any ["amy"]:
            attribute amyeyes_normal default


        group vindick auto if_any ["amy"]:
            attribute vinout default


        attribute vincum null
        group vincum auto if_all ["amy", "vincum"] if_not ["vincomdom"]


        attribute vincondom null
        group vincondom if_all ["amy", "vincondom"] if_not ["vincum"]:
            attribute vinout
        group vincondom if_all ["amy", "vincondom"]:
            attribute vinvaginal
        group vincondomcum auto if_all ["amy", "vincondom", "vincum"]


        attribute violaine


        attribute violaine_bodycum if_any ["violaine"]


        attribute violainebounce if_any ["violaine"]


        attribute violainetongue if_any ["violaine"]
        group violaineeyes auto if_any ["violaine"]:
            attribute violaineeyes_normal default


        group mikedick auto if_all ["violaine"]:
            attribute mikeout null default
        group mikedick auto variant "mikeout" if_all ["violaine", "mikeout"]


        attribute mikecum null
        group mikecum auto if_all ["violaine", "mikecum"] if_not ["mikecondom"]
        group mikecum auto variant "mikeout" if_all ["violaine", "mikecum", "mikeout"] if_not ["mikecondom"]


        attribute mikecondom null
        group mikecondom auto if_all ["violaine", "mikecondom"]
        group mikecondom auto variant "mikeout" if_all ["violaine", "mikecondom", "mikeout"] if_not ["mikecum"]
        group mikecondomcum auto variant "mikeout" if_all ["violaine", "mikecondom", "mikecum", "mikeout"]


        group mikehand auto if_any ["violaine"]:
            attribute onmike default

    layeredimage goth 4some bj:


        always "goth_4some_bj_bg"


        attribute violaine
        always "goth_4some_bj_violainehead_violainenormal" if_any ["violaine"] if_not ["violaineblowjob"]
        always "goth_4some_bj_violainehead_violainenormal" if_all ["violaine", "violaineblowjob"] if_not ["violaineback"]
        attribute violaineback null
        always "goth_4some_bj_violainehead_violaineback" if_all ["violaine", "violaineblowjob", "violaineback"]


        attribute violaine_blush if_any ["violaine"] if_not ["violaineblowjob"]:
            "goth_4some_bj_violaine_blush_violainenormal"
        attribute violaine_blush if_all ["violaine", "violaineblowjob"] if_not ["violaineback"]:
            "goth_4some_bj_violaine_blush_violainenormal"
        attribute violaine_blush if_all ["violaine", "violaineblowjob", "violaineback"]:
            "goth_4some_bj_violaine_blush_violaineback"


        group violaineeyes auto if_any ["violaine"] if_not ["violaineblowjob"]:
            attribute violaineeyes_normal default
        group violaineeyes auto if_all ["violaine", "violaineblowjob"] if_not ["violaineback"]:
            attribute violaineeyes_normal default
        group violaineeyes auto variant "violaineback" if_all ["violaine", "violaineblowjob", "violaineback"]:
            attribute violaineeyes_normal default


        group violainemouths auto if_any ["violaine"] if_not ["violaineblowjob"]:
            attribute violainemouth_closed default
        attribute violaineblowjob if_any ["violaine"] if_not ["violaineback"]


        group violaineblowjob auto if_all ["violaine", "violaineblowjob"] if_not ["violaineback"]
        group violaineblowjob auto variant "violaineback" if_all ["violaine", "violaineblowjob", "violaineback"]
        attribute violaine_mouthcum if_all ["violaine", "violainemouth_open"] if_not ["violaineblowjob"]


        attribute violaine_facecum if_any ["violaine"] if_not ["violaineblowjob"]:
            "goth_4some_bj_violaine_facecum_violainenormal"
        attribute violaine_facecum if_all ["violaine", "violaineblowjob"] if_not ["violaineback"]:
            "goth_4some_bj_violaine_facecum_violainenormal"
        attribute violaine_facecum if_all ["violaine", "violaineblowjob", "violaineback"]:
            "goth_4some_bj_violaine_facecum_violaineback"


        attribute amy
        always "goth_4some_bj_amyhead_amynormal" if_any ["amy"] if_not ["amyblowjob"]
        always "goth_4some_bj_amyhead_amynormal" if_all ["amy", "amyblowjob"] if_not ["amyback"]
        attribute amyback null
        always "goth_4some_bj_amyhead_amyback" if_all ["amy", "amyblowjob", "amyback"]


        group amyeyes auto if_any ["amy"] if_not ["amyblowjob"]:
            attribute amyeyes_normal default
        group amyeyes auto if_all ["amy", "amyblowjob"] if_not ["amyback"]:
            attribute amyeyes_normal default
        group amyeyes auto variant "amyback" if_all ["amy", "amyblowjob", "amyback"]:
            attribute amyeyes_normal default


        group amymouths auto if_any ["amy"] if_not ["amyblowjob"]:
            attribute amymouth_closed default
        attribute amyblowjob if_any ["amy"] if_not ["amyback"]


        group amyblowjob auto if_all ["amy", "amyblowjob"] if_not ["amyback"]
        group amyblowjob auto variant "amyback" if_all ["amy", "amyblowjob", "amyback"]
        attribute amy_mouthcum if_all ["amy", "amymouth_open"] if_not ["amyblowjob"]


        attribute amy_facecum if_any ["amy"] if_not ["amyblowjob"]:
            "goth_4some_bj_amy_facecum_amynormal"
        attribute amy_facecum if_all ["amy", "amyblowjob"] if_not ["amyback"]:
            "goth_4some_bj_amy_facecum_amynormal"
        attribute amy_facecum if_all ["amy", "amyblowjob", "amyback"]:
            "goth_4some_bj_amy_facecum_amyback"


        attribute mikeout if_not ["amyblowjob"]
        attribute mikeout if_any ["amyblowjob"] if_not ["amy"]


        group mikecum auto if_any ["mikecum"] if_not ["amyblowjob"]
        group mikecum auto if_all ["mikecum", "amyblowjob"] if_not ["amy"]


        attribute mikehand null
        group mikehand auto if_all ["mikehand", "mikeout"] if_not ["amyblowjob"]:
            attribute mikedown default
        group mikehand auto if_all ["mikehand", "mikeout", "amyblowjob"] if_not ["amy"]:
            attribute mikedown default


        attribute vinout if_not ["amyblowjob"]
        attribute vinout if_any ["amyblowjob"] if_not ["amy"]


        group vincum auto if_any ["vincum"] if_not ["amyblowjob"]
        group vincum auto if_all ["vincum", "amyblowjob"] if_not ["amy"]


        attribute vinhand null
        group vinhand auto if_all ["vinhand", "vinout"] if_not ["amyblowjob"]:
            attribute vindown default
        group vinhand auto if_all ["vinhand", "vinout", "amyblowjob"] if_not ["amy"]:
            attribute vindown default
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
