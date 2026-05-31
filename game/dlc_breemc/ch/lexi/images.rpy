init 1:
    layeredimage bree cunnilingus lexi:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, MCCGPicker], npc=lexi)
        attribute breemc null
        group bg auto:
            attribute bedroom default

        group head auto:
            attribute front default
        group collars auto variant "back" if_any "back"
        group collars auto variant "front" if_any "front"

        group exp auto if_not "back":
            attribute normal default

        group hands auto:
            attribute frontward default
            attribute backward if_not "back"

        always:
            "bree_cunnilingus_lexi_body"

        attribute pubes
        attribute pregnant
        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute tongue null

        attribute dildo null
        group dildo auto if_any "dildo"

        attribute anal_gape

        attribute beads null
        group beads auto if_any "beads"

        attribute pussy_gape

        group tongue auto if_any "lick" if_not "nomc"

        attribute nomc null
        attribute mc_haircut null
        attribute mc_nohaircut null
        attribute mc_pubes null
        attribute mc_casual null

        group breemc auto variant "mc_haircut" if_any "mc_haircut" if_not "nomc":
            attribute suck default
        group breemc auto variant "mc_nohaircut" if_any "mc_nohaircut" if_not "nomc"
        attribute mc_pregnant null
        group mc_pregnant auto if_any "mc_pregnant"

        group multiple auto variant mcpiercings_lick when lick and not nomc
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute tongue null
        group multiple auto variant mcpiercings_suck when suck and not nomc
        group multiple:
            attribute mc_ears null
            attribute mc_lips null
            attribute mc_navel null
            attribute mc_pregnant_navel null
            attribute tongue null

    layeredimage bree lick lexi:
        attribute_function MultiPickers([CollarPicker, OutfitPicker,PiercingsPicker, MCCGPicker], npcs=[lexi])

        attribute breemc null
        attribute lexi null

        group bg auto:
            attribute park default

        always:
            "bree_lick_lexi_body"

        attribute naked null
        group outfit auto if_not ["naked"]

        attribute mc_naked null
        attribute mc_pubes null
        attribute mc_nohaircut null
        attribute mc_haircut
        group mcoutfit auto if_not ["mc_naked"]

        attribute lexi_collar

        group multiple auto variant piercings
        group multiple:
            attribute lexi_clit null
            attribute mc_ears null

    layeredimage lexi cunnilingus bree:
        attribute_function Pickers([CollarPicker, PiercingsPicker, MCCGPicker], npc=lexi)
        attribute mc_casual null
        always:
            "lexi_cunnilingus_bree_bg_bedroom"

        attribute breemc

        attribute mc_collar
        attribute mc_pubes
        attribute mc_haircut
        attribute mc_nohaircut null

        attribute mc_pregnant

        group lexi_position:
            attribute back default
            attribute front

        attribute lexi_collar
        group multiple auto variant piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute navel null
            attribute pregnant_navel null
            attribute nipples null
            attribute tongue null

        group multiple auto variant mcpiercings
        group multiple:
            attribute mc_ears null

        group mchands auto:
            attribute pose1 default

        attribute vibrator

        group mceyes auto:
            attribute opened default

        group multiple auto variant lexihand when back
        group leximouth auto if_any "back":
            attribute smile default


    layeredimage lexi fingering bree:
        attribute_function Pickers([PregnancyPicker, PiercingsPicker, MCCGPicker], npc=lexi)

        attribute breemc
        attribute naked null
        attribute pregnant null
        attribute mc_casual null
        attribute mc_halloween null
        attribute mc_collar null
        attribute mc_pubes null
        attribute mc_haircut null
        attribute mc_nohaircut null


        group bg auto:
            attribute bedroom default


        always:
            "lexi_fingering_bree_bodies"

        always:
            "lexi_fingering_bree_exp_lexi_normal"


        group mceyes auto:
            attribute pleasure default


        group multiple auto variant pregnancy

        group multiple auto variant piercings:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null

        group multiple auto variant mcpiercings:
            attribute clit null


        group multiple auto variant outfits_lexi when halloween and not naked
        group multiple auto variant outfits_lexi_pregnant when halloween and pregnant and not naked

        always "lexi_fingering_bree_outfits_mc_halloween" if_not ["naked"] if_any ["halloween"]
        always "lexi_fingering_bree_outfits_mc_nopregnant_halloween" if_not ["pregnant", "naked"] if_any ["halloween"]
        always "lexi_fingering_bree_outfits_mc_pregnant_halloween" if_not ["naked"] if_all ["pregnant", "halloween"]


        group fx auto


        group fg auto


    layeredimage bree licking lexi:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, MCCGPicker], npc=lexi)

        attribute breemc
        attribute naked null
        attribute pregnant null
        attribute mc_naked null
        attribute mc_casual null
        attribute mc_halloween null
        attribute mc_pubes null
        attribute mc_haircut null
        attribute mc_nohaircut null


        group bg auto:
            attribute bedroom default


        always:
            "bree_licking_lexi_bodies"


        group collars auto


        group leyes auto:
            attribute normal default


        group multiple auto variant pregnancy


        group multiple auto variant mcpiercings:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null
            attribute tongue null


        group multiple auto variant outfits_lexi when halloween and not naked
        group multiple auto variant outfits_lexi_pregnant when halloween and pregnant and not naked

        always "bree_licking_lexi_outfits_mc_halloween" if_not ["naked"] if_any ["halloween"]
        always "bree_licking_lexi_outfits_mc_pregnant_halloween" if_not ["naked"] if_all ["pregnant", "halloween"]


        group multiple auto variant piercings:
            attribute clit null
            attribute nipples when naked
            attribute halloween_nipples when halloween and not naked


    layeredimage lawyers ending:
        attribute_function Pickers([MCCGPicker, EndingKidPicker], npc=lexi)

        attribute breemc null
        attribute mc_nohaircut null
        attribute mc_casual null
        attribute mc_clit null
        attribute mc_ears null
        attribute mc_lips null
        attribute mc_navel null
        attribute mc_nipples null
        attribute mc_nose null
        attribute mc_pubes null
        attribute mc_tongue null


        always "lawyers_ending_bg"


        attribute bree
        attribute lexi


        attribute mc_pregnant null
        group baby auto if_any ["mc_pregnant"]:
            attribute white default
            attribute afro
            attribute latin

        group baby_white_hair auto if_any ["mc_pregnant"] if_not ["afro", "latino"]:
            attribute black
            attribute blond default
            attribute brown
            attribute red

    layeredimage whores ending:

        attribute_function Pickers([PregnancyPicker, CollarPicker, PiercingsPicker, MCCGPicker, EndingKidPicker], npc=lexi)

        attribute breemc null
        attribute mc_nohaircut null
        attribute mc_casual null
        attribute mc_pubes null


        always "whores_ending_bg"


        always "whores_ending_bree"
        always "whores_ending_lexi"


        always "whores_ending_nobaby" if_not ["mc_pregnant"]


        group multiple auto variant pregnancy









        group collars auto


        group multiple auto variant piercings
        group multiple:
            attribute mc_clit null
            attribute mc_nipples null
            attribute mc_navel null
            attribute lexi_clit null


        always "whores_ending_fg"


    layeredimage nice ending:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, MCCGPicker, EndingKidPicker], npc=lexi)

        attribute breemc null
        attribute mc_nohaircut null
        attribute mc_casual null
        attribute mc_pubes null
        attribute mc_ears null
        attribute clit null
        attribute navel null
        attribute pregnant_navel null
        attribute nipples null


        always "nice_ending_bg"


        attribute mc_pregnant null
        group kid auto if_any ["mc_pregnant"]:
            attribute white default

        group kid_white_hair auto if_any ["mc_pregnant"] :
            attribute black
            attribute blond default
            attribute brown


        attribute bree


        group multiple auto variant pregnancy_mc


        group multiple auto variant piercings_mc when bree


        always "nice_ending_counter"


        attribute lexi


        group multiple auto variant pregnancy_lexi


        group multiple auto variant piercings_lexi when lexi


        group collars auto

    layeredimage escorts ending:
        attribute_function Pickers([CollarPicker, PregnancyPicker, PiercingsPicker, MCCGPicker, EndingKidPicker], npc=lexi)

        attribute breemc null
        attribute mc_nohaircut null
        attribute mc_casual null
        attribute mc_clit null
        attribute mc_ears null
        attribute mc_lips null
        attribute mc_navel null
        attribute mc_nipples null
        attribute mc_nose null
        attribute mc_pubes null
        attribute mc_tongue null
        attribute clit null
        attribute lips null
        attribute navel null
        attribute nipples null
        attribute nose null
        attribute mc_pubes null
        attribute tongue null


        always "escorts_ending_bg"


        attribute bree


        group multiple auto variant pregnancy_mc


        group multiple auto variant piercings_mc when bree


        attribute lexi


        group multiple auto variant pregnancy_lexi


        group multiple auto variant piercings_lexi when lexi


        group collars auto


        attribute mc_pregnant null
        group baby auto if_any ["mc_pregnant"]:
            attribute white default
            attribute afro
            attribute latin
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
