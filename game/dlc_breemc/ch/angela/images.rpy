init 1:
    layeredimage angela kiss:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, MCCGPicker], npc=angela)

        attribute breemc null
        attribute mc_pubes null

        always "angela_kiss_bodies" if_not ["bowsette"]
        attribute bowsette "angela_kiss_bodies_bowsette"

        attribute mc_nohaircut null
        attribute mc_haircut if_not "bowsette"


        group multiple auto variant piercings
        group multiple auto variant piercings_casual when not (date or wedding)
        group multiple auto variant piercings_date when date
        group multiple auto variant piercings_wedding when wedding
        group multiple:
            attribute clit null
            attribute navel null
            attribute pregnant_navel null


        group collars auto


        attribute naked null
        attribute topless null
        group outfits auto if_not ["naked", "topless"]:
            attribute chinese "angela_kiss_outfits_casual"
            attribute bowsette "angela_kiss_outfits_halloween"
            attribute invisible "angela_kiss_outfits_halloween"

        group multiple auto variant mcpiercings if_not ["bowsette"]
        group mcoutfits auto if_not ["naked", "topless"]


        group necklace auto if_not ["collar"]


        always "angela_kiss_hairdetail_angela"
        group mchairdetail auto if_not ["bowsette"]


    layeredimage angela cunnilingus bree:
        attribute_function Pickers([CollarPicker, PiercingsPicker, MCCGPicker], npc=angela)

        attribute hotel null

        group bg auto:
            attribute bedroom default

        attribute breemc
        attribute mc_pubes
        attribute mc_pregnant

        attribute mc_collar

        group mc_head:
            attribute up null default
            attribute down null

        group head auto variant "up" if_any "up"
        group head auto variant "down" if_any "down"

        group exp auto variant "up" if_any "up":
            attribute normal default
        group exp auto variant "down" if_any "down"

        group multiple auto variant mc_piercings

        group mc_hands auto if_not "onangela":
            attribute neck default

        attribute mc_casual null
        attribute mc_date null


        attribute nonpc null

        group hands auto

        group angela auto if_not "nonpc":
            attribute kiss default

        group multiple auto variant piercings
        group multiple:
            attribute ears null

        group multiple auto variant piercings_kiss when kiss and not nonpc
        group multiple auto variant piercings_lick when lick and not nonpc
        group multiple auto variant piercings_suck when suck and not nonpc

        group mc_hands auto if_all ["onangela", "kiss"]

    layeredimage bree cunnilingus angela:
        attribute_function Pickers([CollarPicker, PiercingsPicker, PubesPicker, PregnancyPicker, MCCGPicker], npc=angela)
        attribute breemc null
        attribute hotel null
        group bg auto:
            attribute bedroom default

        always:
            "bree_cunnilingus_angela_body"

        group head auto:
            attribute front default

        attribute collar

        group exp auto variant "side" if_any "side":
            attribute normalangela default

        group exp auto variant "front" if_any "front"

        group hands auto

        attribute pubes
        group multiple auto variant piercings
        group multiple:
            attribute ears null
            attribute tongue null

        attribute tongue null
        group tongue auto if_any "tongue" if_not ["normalangela", "normaldown", "nomalside"]

        attribute nomc null
        group breemc auto if_not "nomc":
            attribute suck default

        attribute mc_casual null
        attribute mc_nohaircut null
        group haircuts auto variant "kiss" if_any "kiss" if_not "nomc"
        group haircuts auto variant "suck" if_any "suck" if_not "nomc"
        group haircuts auto variant "lick" if_any "lick" if_not "nomc"

        group mc_hands auto if_not "nomc"

        group mc_exp auto variant "kiss" if_any "kiss" if_not "nomc":
            attribute normalbree default

        group mc_exp auto variant "suck" if_any "suck" if_not "nomc"

        group fx auto variant "suck" if_any "suck" if_not "nomc"

        attribute mc_ears null
        group multiple auto variant mc_piercings_kiss when kiss and not nomc
        group multiple auto variant mc_piercings_suck when suck and not nomc

    layeredimage angela missionary bree:
        attribute_function Pickers([PiercingsPicker, MCCGPicker], npc=angela)

        attribute mc_casual null
        attribute mc_date null
        attribute mc_pubes null

        group bg auto:
            attribute bedroom default

        group shade auto

        attribute breemc null
        always:
            "angela_missionary_bree_bodies"

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute mc_collar

        attribute mc_pregnant

        attribute squirt

        group exp auto:
            attribute pleasure default

        group multiple auto variant mc_piercings
        group multiple:
            attribute mc_tongue null

        group multiple auto variant angela_piercings
        group multiple:
            attribute clit null
            attribute ears null
            attribute lips null
            attribute navel null
            attribute pregnant_navel null

    layeredimage bree missionary angela:
        attribute_function Pickers([PiercingsPicker, MCCGPicker], npc=angela)

        attribute mc_casual null
        attribute mc_date null
        attribute mc_sexydate null

        group bg auto:
            attribute bedroom default

        group shade auto

        attribute breemc null
        always:
            "bree_missionary_angela_bodies"

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute mc_collar

        attribute mc_pregnant

        attribute squirt

        group exp auto:
            attribute normal null default

        group multiple auto variant mc_piercings
        group multiple:
            attribute mc_ears null

        group multiple auto variant angela_piercings
        group multiple:
            attribute ears null

    layeredimage angela dylan ending:
        attribute_function Pickers([OutfitPicker, PiercingsPicker, MCCGPicker], npc=angela)
        attribute naked null

        attribute bg

        group multiple auto variant fx

        attribute hands

        always:
            "angela_dylan_ending_bodies"

        attribute mc_pregnant

        group multiple auto variant hidden_piercings

        group mc_outfits auto if_not "naked"
        group mc_outfits auto variant "pregnant" if_any "mc_pregnant" if_not "naked"

        group outfits auto if_not "naked"

        always:
            "angela_dylan_ending_angela"

        group haircuts auto

        group neck auto if_not "naked"

        group multiple auto variant piercings

        group expangela auto:
            attribute angelanormal default

        group expmc auto:
            attribute mcnormal default


    layeredimage angela mike ending:
        attribute_function Pickers([MCCGPicker])
        always:
            "angela_mike_ending_bg"
        always:
            "angela_mike_ending_mike"

        group left_hand auto:
            attribute still default

        attribute breemc
        attribute mc_pregnant

        group multiple auto variant piercings

        group haircuts auto

        attribute mc_collar

        attribute leash

        always:
            "angela_mike_ending_right_hand"

    layeredimage angela solo ending:
        attribute_function Pickers([PregnancyPicker], npc=angela)

        always:
            "angela_solo_ending_bg"

        always:
            "angela_solo_ending_body"

        attribute pregnant null

        always:
            if_any "pregnant"
            "angela_solo_ending_shadow"

        group boy auto if_any "pregnant":
            attribute white default

        group hairs auto if_any "pregnant" if_not ["black", "latino"]:
            attribute brown default

    layeredimage angela ending:
        attribute_function Pickers([PregnancyPicker, MCCGPicker], npc=angela)

        always:
            "angela_ending_bg"

        always:
            "angela_ending_angela"

        attribute pregnant null
        attribute mc_pregnant null

        always:
            if_any ["pregnant", "mc_pregnant"]
            "angela_ending_shadow"

        group boy auto if_any ["pregnant", "mc_pregnant"]:
            attribute white default

        group hairs auto if_any ["pregnant", "mc_pregnant"] if_not ["black", "latino"]:
            attribute brown default

        attribute breemc
        group haircuts auto


    layeredimage magicshow:
        zoom 0.5
        attribute_function Pickers([MCCGPicker])


        always:
            "magicshow_house"

        group breemc auto:
            attribute dodge default


        always:
            "magicshow_doves"


        always:
            "magicshow_dylan"

    layeredimage angela finger bree:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker, MCCGPicker], npc=angela)

        group multiple:
            attribute breemc null
            attribute clit null
            attribute ears null
            attribute lips null
            attribute nipples null
            attribute navel null
            attribute pregnant_navel null
            attribute mc_ears null
            attribute mc_pregnant_navel null

        group bg auto:
            attribute bedroom4 default

        always "angela_finger_bree_bodies"

        attribute mc_nohaircut null
        attribute mc_haircut

        attribute pregnant

        attribute blush

        attribute mc_pubes

        attribute naked null
        group mc_bot auto when not (naked or mc_naked)
        attribute mc_pregnant
        group mc_top auto when not (naked or mc_naked)

        group outfit auto when not naked
        group outfit auto variant pregnant when pregnant and not naked

        group exp auto:
            attribute normal default

        attribute mc_collar

        group multiple auto variant mc_piercings

        group piercings auto

        group multiple auto variant fx
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
