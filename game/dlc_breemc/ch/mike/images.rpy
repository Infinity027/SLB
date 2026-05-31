init 1:
    layeredimage mike kiss:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=mike)

        attribute breemc null
        attribute mc_pregnant null
        attribute mc_pubes null

        group dick:
            attribute small null
            attribute medium null
            attribute big null

        always "mike_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "mike_kiss_bodies_bowsette"

        group haircuts auto if_not ["bowsette"]:
            attribute mc_nohaircut null

        attribute naked null
        attribute topless null


        group outfits auto if_not ["naked", "topless"]:
            attribute sleep null
            attribute sport null
            attribute swimsuit null
            attribute towel null
            attribute underwear null
            attribute chinese "mike_kiss_outfits_casual"
            attribute bowsette "mike_kiss_outfits_halloween"
            attribute invisible "mike_kiss_outfits_halloween"


        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null
        group mcoutfits auto if_not ["mc_naked", "mc_topless"]

    layeredimage mike spoon:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=mike)

        attribute breemc null
        attribute casual null
        attribute mc_casual null

        attribute medium null


        group bg auto:
            attribute bedroom4 default


        always "mike_spoon_bodies"
        always "mike_spoon_mike"

        attribute mc_nohaircut null
        attribute mc_haircut


        attribute mc_collar

        attribute mc_pubes

        group multiple auto variant piercings_behind


        attribute mc_pregnant


        group multiple auto variant piercings
        group multiple:
            attribute mc_lips null
            attribute mc_tongue null
            attribute mc_ears null


        attribute speed


        always "mike_spoon_head_mike"


        attribute sweat


        attribute bodycum


        group dick auto:
            attribute out default


        attribute dickcum if_all ["dickcum", "out"] if_not ["condom"]


        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]


        attribute condom null
        group condom auto if_any ["condom"]
        group condomcum auto if_all ["condom", "cum"]


        group expeyes auto:
            attribute eyes_closed default
        group expmouth auto:
            attribute mouth_pleasure default
        attribute breath if_not ["mouth_pain"]


        group arm auto:
            attribute pull default
        attribute speedfinger if_all ["speedfinger", "finger"]


        attribute squirt

    layeredimage mike doggy:
        attribute_function Pickers([MCCGPicker, NPCPicker], npc=mike)

        attribute mc_casual null
        attribute mc_pubes null
        attribute mc_nohaircut null


        attribute noone null

        group bg auto:
            attribute bedroom4 default

        attribute breemc

        group dick auto:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group mike variant "front" auto if_any "front" if_not ['noone']
        group mike variant "back" auto if_any "back" if_not ['noone', 'sasha']
        group dick variant "back" auto if_any "back" if_not ['noone', 'sasha']

        group face auto:
            attribute back default

        attribute mc_haircut

        attribute mc_collar

        group multiple auto variant piercings
        group multiple:
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        attribute mc_pregnant

        attribute pull null
        group pull auto if_any ["pull"] if_not ["mc_haircut"]
        group pull auto variant "haircut" if_all ["pull", "mc_haircut"]

        attribute condom null
        group condom auto if_any "condom" if_not "noone"
        group condom auto variant "back" if_all ["condom", "back"] if_not ["noone", "cumshot"]
        group condomcum auto if_all ["condom", "cumshot", "back"] if_not "noone"

        attribute cumshot null
        group cumshot auto if_any "cumshot"
        group cumshot auto variant "back" if_all ["cumshot", "back"] if_not ["condom"]

        group multiple auto variant cum

        group eyes auto:
            attribute normal default

        group mouth auto if_any "back":
            attribute normal default

        attribute sasha

        group toy auto
        group toy auto variant "dildo" if_any ["dildoin", "dildoout"]
        group mike variant "back" auto if_all ["back", "beads"] if_not ['noone', 'sasha'] if_any ["cumshot", "cumonass"]

        group multiple auto variant fx


    layeredimage mike rough doggy:
        attribute_function Pickers([DayNightPicker, NPCPicker, MCCGPicker], npc=mike)

        attribute mc_casual null

        group bg auto:
            attribute bedroom4 null default

        group bg auto variant "day" if_any "day"
        group bg auto variant "night" if_any "night"
        always "mike_rough_doggy_mc_haircut_reflexion" if_any ["mc_haircut"]

        attribute breemc

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute mc_pubes null

        attribute mc_pregnant

        attribute mc_collar

        attribute blush

        group exp auto:
            attribute normal default

        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_lips null
            attribute mc_pregnant_navel null
            attribute mc_tongue null

        group dick auto:
            attribute out null default
        group dick auto variant "out" if_any ["out"]

        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum"]

        attribute cum null
        group cum auto if_any ["cum"] if_not ["condom"]
        group cum auto variant "out" if_all ["cum", "out"] if_not ["condom"]

        group condomcum auto if_all ["condom", "cum", "out"]

        attribute dickcum null
        group dickcum auto if_all ["dickcum", "out"] if_not ["condom"]

        attribute bodycum

        attribute boobs


    layeredimage mike cowgirl:
        attribute_function Pickers([OutfitPicker, MCCGPicker], npc=mike)

        attribute breemc null


        group bg auto:
            attribute bedroom4 default

        group bodies auto:
            attribute naked default

        group mike_outfit auto


        attribute mc_nohaircut null
        attribute mc_haircut null
        group haircut auto if_any "mc_haircut"


        group acc_stockings auto if_not ["noacc"]


        attribute mc_collar


        attribute blush



        group eyes auto:
            attribute down default

        group mouth auto:
            attribute smile default


        group acc_cap auto if_not ["noacc"]


        group top auto:
            attribute mc_naked null


        attribute mc_pregnant


        attribute mc_pubes


        group bot auto variant "out" if_any "out" if_not ["mc_pregnant", "onass", "onpussy"]
        group bot auto variant "out_pregnant" if_all ["out", "mc_pregnant"] if_not ["onass", "onpussy"]
        group bot auto variant "resting" if_any "resting" if_not ["mc_pregnant", "onass", "onpussy"]
        group bot auto variant "resting_pregnant" if_all ["resting", "mc_pregnant"] if_not ["onass", "onpussy"]


        group dick auto:
            attribute resting null default
            attribute out null
            attribute anal
            attribute vaginal

        group dick auto variant "out" if_any "out"
        group dick auto variant "resting" if_any "resting"



        group bot auto variant "anal" if_any ["anal", "onass"] if_not "mc_pregnant"
        group multiple auto variant bot_anal_pregnant when mc_pregnant and (anal or onass)
        group bot auto variant "vaginal" if_any ["vaginal", "onpussy"] if_not "mc_pregnant"
        group multiple auto variant bot_vaginal_pregnant when mc_pregnant and (vaginal or onpussy)


        attribute creampie null
        group creampie auto if_any ["creampie"] if_not ["condom"]


        attribute cum null
        group multiple auto variant cum when cum
        group cum auto variant "pregnant" if_all ["cum", "mc_pregnant"]
        group cum auto variant "nopregnant" if_any ["cum"] if_not ["mc_pregnant"]


        attribute condom null
        group condom auto if_any ["condom"] if_not ["cum", "condomcum"]
        group condom auto variant "out" if_all ["condom", "out"] if_not ["cum", "condomcum"]

        attribute condomcum null
        group condomcum auto if_all ["condom", "condomcum"]


        attribute dickcum null
        group dickcum auto if_any "dickcum"


        attribute cumshot null
        group cumshot auto if_any "cumshot"


        group multiple auto variant piercings_vaginal when vaginal
        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_tongue null
            attribute mc_lips null

        group fx auto

    layeredimage breemc titfuck:
        attribute_function Pickers([OutfitPicker, MCCGPicker])

        attribute breemc null

        attribute casual null
        attribute mc_casual null

        attribute mc_pubes null
        attribute mc_pregnant null


        group bg auto:
            attribute livingroom default


        group body auto:
            attribute mike default
        group malepubes auto


        group boobs auto:
            attribute down default


        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute mc_tongue null


        attribute mc_nipples null
        group nipples auto if_any ["mc_nipples"]


        group dickmike auto variant "up" if_all ["mike", "up"]
        group dickmike auto variant "down" if_all ["mike", "down"]
        group dickdwayne auto if_any ["dwayne"]
        group dickjack auto if_any ["jack"]
        group dickscottie auto if_any ["scottie"]


        group head auto:
            attribute normal default

        attribute mc_nohaircut null
        attribute mc_haircut null
        group haircut auto if_any "mc_haircut"

        attribute mc_collar null
        group collar auto if_any ["mc_collar"]

        group exp auto if_any ["normal"]:
            attribute smile default
        group eyes auto if_any ["normal"]:
            attribute open null default
        group eyes auto variant "facecum" if_all ["normal", "facecum"]
        group eyes auto variant "nofacecum" if_any ["normal"] if_not ["facecum"]


        attribute mc_nose null
        group nose auto if_any ["mc_nose"]


        attribute cum null
        group cum auto if_any ["cum"]
        attribute dickcum if_any ["down"]
        attribute tonguecum null
        group tonguecum auto if_all ["tonguecum", "tongueout", "normal"]
        always "breemc_titfuck_tonguecum_lick" if_all ["tonguecum", "lick"]
        attribute facecum


        group hands auto
        group belly auto

    layeredimage mike missionary:
        attribute_function Pickers([MCCGPicker, NPCPicker], npc=mike)

        attribute breemc null


        group bg auto:
            attribute bedroom4 default


        group body auto:
            attribute mc_naked default

        attribute mc_haircut
        attribute mc_nohaircut null


        group expressions auto:
            attribute normal null default
            attribute pleasure null
            attribute ahegao null

        group exp auto variant "bowsette" if_any ["bowsette"]
        group exp auto variant "naked" if_not ["bowsette"]


        always "mike_missionary_legs" if_any ["bowsette"] if_not ["mc_naked"]


        attribute mc_pregnant


        attribute mc_pubes


        group multiple auto variant piercings
        group multiple:
            attribute mc_ears null
            attribute mc_nose null

        group multiple auto variant piercings_normal when normal
        group multiple auto variant piercings_pleasure when pleasure
        group multiple auto variant piercings_ahegao when ahegao


        attribute bowsette if_not ["mc_naked", "pregnant"]


        attribute arm
        always "mike_missionary_mike"


        attribute bellycum
        attribute boobycum


        group pussy auto


        group dicks auto:
            attribute outside null default
            attribute vaginal
            attribute anal

        group dicks auto variant "outside" if_any "outside"


        attribute condom null
        group condom auto if_any ["condom"]
        group condom auto variant "outside" if_all ["condom", "outside"]

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute creampie null
        group creampie auto if_any "creampie"

        group condomcum auto if_all ["condom"] if_any ["cumshot", "creampie"]


        attribute cum null
        group cum auto if_any ["cum"]


        attribute xray null

        group xray_bg auto if_any "xray"


        group xray_creampie auto if_all ["xray", "creampie"] if_not ["condom"]


        group xray_condom auto if_all ["xray", "condom"] if_not ["cum"]


        group xray_condomcum auto variant "xray" if_all ["condom", "xray"] if_any ["cumshot", "creampie"]

    layeredimage mike lapdance:
        attribute_function Pickers([OutfitPicker], npc=mike)

        always "mike_lapdance_bg"
        group outfit auto:
            attribute casual default

        attribute nomc null
        always "mike_lapdance_breemc" if_not "nomc"

        group exp auto if_not "nomc":
            attribute normal default

        group multiple auto variant piercings_breemc when not nomc
        group multiple auto variant piercings_breemc_ahegao when ahegao and not nomc
        group multiple auto variant piercings_breemc_notahegao when not (ahegao or nomc)

        attribute bree_naked null
        always "mike_lapdance_breemc_sexyoutfit" if_not ["nomc", "naked","bree_naked"]

        group arm auto if_not ["fuck", "nomc"]

        always "mike_lapdance_fg"
        always "mike_lapdance_light"

        attribute fuck

    layeredimage mike reverse cowgirl:
        attribute_function Pickers([PiercingsPicker, MCCGPicker], npc=mike)

        group bg auto:
            attribute bedroom4 default

        always "mike_reverse_cowgirl_bree"

        attribute mc_collar
        attribute mc_haircut
        attribute mc_pregnant

        attribute mc_pubes null
        group pubes auto if_any "mc_pubes":
            attribute haircut if_any "mc_haircut"
            attribute haircut if_any "mc_nohaircut"

        group multiple auto variant piercings

        group fx auto

        group exp auto:
            attribute normal default

        always "mike_reverse_cowgirl_mike"

        group dick_position:
            attribute out null default
            attribute vaginal null
            attribute anal null

        group dick auto variant "out" if_any "out"
        group dick auto if_not "out"

        attribute creampie null
        group creampie auto if_any "creampie"

        attribute condom null
        group condom auto variant "out" if_all ["out", "condom"]
        group condom auto if_not "out" if_all "condom"

        attribute hand null
        group hand auto if_any "hand":
            attribute up default

        attribute cumshot null
        group cumshot auto if_any "cumshot"

        attribute cum null
        group condomcum auto if_all ["condom", "cum"]

    layeredimage mike beats:
        attribute_function MultiPickers([MCCGPicker, OutfitPicker], npcs=[mike], append_npc_from_attributes=True)

        attribute nomc null
        attribute naked null


        attribute breemc if_not ["nomc"]
        attribute mc_haircut if_not ["nomc"]
        attribute mc_pregnant if_not ["nomc"]
        group multiple auto variant mc_piercings when not nomc
        group mc_outfit auto if_not ["nomc", "naked"]
        group mc_pregnant_outfit auto if_any ["mc_pregnant"] if_not ["nomc", "naked"]
        attribute mc_collar if_not ["nomc"]


        group foe auto
        group foe_outfit auto if_not ["naked"]


        always "mike_beats_mike"
        group outfit auto if_not ["naked"]

        always "mike_beats_fx"


    layeredimage mike shower bj:
        attribute_function Pickers([MCCGPicker], npc=mike)

        always:
            "mike_shower_bj_bg"
        always:
            "mike_shower_bj_mike_leg"

        attribute breemc
        attribute mc_pregnant

        group multiple auto variant piercings

        attribute bodycum

        attribute facial

        attribute cumshot

        always:
            "mike_shower_bj_mike"

        group dick auto:
            attribute up default

    layeredimage mike ending:
        attribute_function Pickers([MCCGPicker, EndingKidPicker])
        attribute breemc

        attribute mc_haircut
        attribute mc_nohaircut null
        attribute mc_pregnant null
        attribute mc_pubes null

        group multiple auto variant piercings

        attribute mc_collar

        group kids auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
