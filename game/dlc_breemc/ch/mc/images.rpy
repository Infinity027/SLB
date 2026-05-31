init 1:
    layeredimage breemc:
        attribute_function Pickers([MCPicker], add_mc_prefix=False)

        attribute breemc null
        attribute nohaircut null

        attribute arms01 null
        attribute arms02 null


        group position auto:
            attribute a default

        attribute p null


        group arms auto variant "d" if_any "d"


        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        attribute collar null
        group collar auto if_all ["collar", "d"]


        group null_exp auto:
            attribute normal null default

        group exp auto variant "a" if_any ["a"]
        group exp auto variant "b" if_any ["b"]
        group exp auto variant "d" if_any ["d"]
        group exp auto variant "z" if_any ["z"]


        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]



        group multiple auto variant piercings_a when a if_not ["navel", "pregnant_navel"]
        group multiple auto variant piercings_a when a and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_a_rpg when a and rpg
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_evil when a and evil
        group multiple auto variant piercings_a_mouthful when a and mouthful
        group multiple auto variant piercings_a_wink when a and wink
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_dazed when a and dazed
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_flirt when a and flirt
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_lose when a and lose
        group multiple auto variant piercings_a_thumb when a and thumb

        group multiple auto variant piercings_b when b if_not ["navel", "pregnant_navel"]
        group multiple auto variant piercings_b when b and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_b_rpg when b and rpg
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_evil when b and evil
        group multiple auto variant piercings_b_mouthful when b and mouthful
        group multiple auto variant piercings_b_wink when b and wink
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_dazed when b and dazed
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_flirt when b and flirt
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_lose when b and lose
        group multiple auto variant piercings_b_thumb when b and thumb

        group multiple auto variant piercings_d when d and not (navel or pregnant_navel)
        group multiple auto variant piercings_d when d and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_d_rpg when d and rpg
        group multiple auto variant piercings_d_sad when d and sad
        group multiple auto variant piercings_d_surprised when d and surprised
        group multiple auto variant piercings_d_evil when d and evil
        group multiple auto variant piercings_d_mouthful when d and mouthful
        group multiple auto variant piercings_d_wink when d and wink
        group multiple auto variant piercings_d_happy when d and happy
        group multiple auto variant piercings_d_angry when d and angry
        group multiple auto variant piercings_d_dazed when d and dazed
        group multiple auto variant piercings_d_annoyed when d and annoyed
        group multiple auto variant piercings_d_flirt when d and flirt
        group multiple auto variant piercings_d_normal when d and normal
        group multiple auto variant piercings_d_cry when d and cry
        group multiple auto variant piercings_d_lose when d and lose
        group multiple auto variant piercings_d_thumb when d and thumb

        group multiple auto variant piercings_z when z and not (navel or pregnant_navel)
        group multiple auto variant piercings_z when z and (navel or pregnant_navel) and not dominatrix
        group multiple auto variant piercings_z_dominatrix when z and dominatrix
        group multiple:
            attribute navel null
            attribute pregnant_navel null
        group multiple auto variant piercings_z_sad when z and sad
        group multiple auto variant piercings_z_surprised when z and surprised
        group multiple auto variant piercings_z_evil when z and evil
        group multiple auto variant piercings_z_mouthful when z and mouthful
        group multiple auto variant piercings_z_wink when z and wink
        group multiple auto variant piercings_z_happy when z and happy
        group multiple auto variant piercings_z_angry when z and angry
        group multiple auto variant piercings_z_dazed when z and dazed
        group multiple auto variant piercings_z_annoyed when z and annoyed
        group multiple auto variant piercings_z_flirt when z and flirt
        group multiple auto variant piercings_z_normal when z and normal
        group multiple auto variant piercings_z_cry when z and cry
        group multiple auto variant piercings_z_lose when z and lose
        group multiple auto variant piercings_z_thumb when z and thumb


        attribute naked null


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "d" if_any ["d"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "z" if_any ["z"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "d" if_any ["d"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "z" if_any ["z"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["topless", "naked"]


        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]
        group stockings auto variant "z" if_all ["z"] if_not ["pregnant", "bottomless", "naked"]
        group stockings auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        group garterbelt auto variant "z" if_all ["z"] if_not ["pregnant"]
        group garterbelt auto variant "z_pregnant" if_all ["z", "pregnant"]


        group arms_outfits auto variant "d_arms01" if_all ["arms01", "d"] if_not ["arms02", "dominatrix"]
        group arms_outfits auto variant "d_arms02" if_all ["arms02", "d"] if_not ["arms01", "dominatrix"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]
        group acc_arm auto variant "d" if_any ["d"]
        group acc_arm auto variant "z" if_any ["z"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]
        group necklace auto variant "d" if_any ["d"] if_not ["collar"]


        group collar auto if_all ["collar"] if_any ["a", "b"]


        attribute leash null
        group leash auto if_any ["leash"]


        group acc_ears auto variant "a" if_any ["a"]
        group acc_ears auto variant "b" if_any ["b"]
        group acc_ears auto variant "d" if_any ["d"]


        group tattoo auto variant "a" if_any ["a"]
        group tattoo auto variant "b" if_any ["b"]
        group tattoo auto variant "d" if_any ["d"]


        group acc_head auto
        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "d" if_any ["d"]

        group acc_waist auto variant "z" if_any ["z"] if_not ["bottomless", "naked"]


        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "d" if_any ["d"]
        group fx auto variant "z" if_any ["z"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "d" if_any ["d"]

    layeredimage breemc close:
        yalign 0.12
        attribute_function Pickers([MCPicker], add_mc_prefix=False)

        attribute breemc null
        attribute nohaircut null

        attribute arms01 null
        attribute arms02 null


        group position auto:
            attribute a default

        attribute p null


        group arms auto variant "d" if_any "d"


        attribute pubes null
        group pubes auto if_any "pubes"


        attribute pregnant null
        group pregnant auto if_any ["pregnant"]


        attribute blush


        attribute collar null
        group collar auto if_all ["collar", "d"]


        group null_exp auto:
            attribute normal null default

        group exp auto variant "a" if_any ["a"]
        group exp auto variant "b" if_any ["b"]
        group exp auto variant "d" if_any ["d"]
        group exp auto variant "z" if_any ["z"]


        group haircuts auto variant "a" if_any ["a"]
        group haircuts auto variant "b" if_any ["b"]
        group haircuts auto variant "d" if_any ["d"]
        group haircuts auto variant "z" if_any ["z"]



        group multiple auto variant piercings_a when a if_not ["navel", "pregnant_navel"]
        group multiple auto variant piercings_a when a and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_a_rpg when a and rpg
        group multiple auto variant piercings_a_sad when a and sad
        group multiple auto variant piercings_a_surprised when a and surprised
        group multiple auto variant piercings_a_evil when a and evil
        group multiple auto variant piercings_a_mouthful when a and mouthful
        group multiple auto variant piercings_a_wink when a and wink
        group multiple auto variant piercings_a_happy when a and happy
        group multiple auto variant piercings_a_angry when a and angry
        group multiple auto variant piercings_a_dazed when a and dazed
        group multiple auto variant piercings_a_annoyed when a and annoyed
        group multiple auto variant piercings_a_flirt when a and flirt
        group multiple auto variant piercings_a_normal when a and normal
        group multiple auto variant piercings_a_cry when a and cry
        group multiple auto variant piercings_a_lose when a and lose
        group multiple auto variant piercings_a_thumb when a and thumb

        group multiple auto variant piercings_b when b if_not ["navel", "pregnant_navel"]
        group multiple auto variant piercings_b when b and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_b_rpg when b and rpg
        group multiple auto variant piercings_b_sad when b and sad
        group multiple auto variant piercings_b_surprised when b and surprised
        group multiple auto variant piercings_b_evil when b and evil
        group multiple auto variant piercings_b_mouthful when b and mouthful
        group multiple auto variant piercings_b_wink when b and wink
        group multiple auto variant piercings_b_happy when b and happy
        group multiple auto variant piercings_b_angry when b and angry
        group multiple auto variant piercings_b_dazed when b and dazed
        group multiple auto variant piercings_b_annoyed when b and annoyed
        group multiple auto variant piercings_b_flirt when b and flirt
        group multiple auto variant piercings_b_normal when b and normal
        group multiple auto variant piercings_b_cry when b and cry
        group multiple auto variant piercings_b_lose when b and lose
        group multiple auto variant piercings_b_thumb when b and thumb

        group multiple auto variant piercings_d when d and not (navel or pregnant_navel)
        group multiple auto variant piercings_d when d and (navel or pregnant_navel) and not rpg
        group multiple auto variant piercings_d_rpg when d and rpg
        group multiple auto variant piercings_d_sad when d and sad
        group multiple auto variant piercings_d_surprised when d and surprised
        group multiple auto variant piercings_d_evil when d and evil
        group multiple auto variant piercings_d_mouthful when d and mouthful
        group multiple auto variant piercings_d_wink when d and wink
        group multiple auto variant piercings_d_happy when d and happy
        group multiple auto variant piercings_d_angry when d and angry
        group multiple auto variant piercings_d_dazed when d and dazed
        group multiple auto variant piercings_d_annoyed when d and annoyed
        group multiple auto variant piercings_d_flirt when d and flirt
        group multiple auto variant piercings_d_normal when d and normal
        group multiple auto variant piercings_d_cry when d and cry
        group multiple auto variant piercings_d_lose when d and lose
        group multiple auto variant piercings_d_thumb when d and thumb

        group multiple auto variant piercings_z when z and not (navel or pregnant_navel)
        group multiple auto variant piercings_z when z and (navel or pregnant_navel) and not dominatrix
        group multiple auto variant piercings_z_dominatrix when z and dominatrix
        group multiple:
            attribute navel null
            attribute pregnant_navel null
        group multiple auto variant piercings_z_sad when z and sad
        group multiple auto variant piercings_z_surprised when z and surprised
        group multiple auto variant piercings_z_evil when z and evil
        group multiple auto variant piercings_z_mouthful when z and mouthful
        group multiple auto variant piercings_z_wink when z and wink
        group multiple auto variant piercings_z_happy when z and happy
        group multiple auto variant piercings_z_angry when z and angry
        group multiple auto variant piercings_z_dazed when z and dazed
        group multiple auto variant piercings_z_annoyed when z and annoyed
        group multiple auto variant piercings_z_flirt when z and flirt
        group multiple auto variant piercings_z_normal when z and normal
        group multiple auto variant piercings_z_cry when z and cry
        group multiple auto variant piercings_z_lose when z and lose
        group multiple auto variant piercings_z_thumb when z and thumb


        attribute naked null


        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "d" if_any ["d"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "z" if_any ["z"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["bottomless", "naked"]
        group bot auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "b" if_any ["b"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "d" if_any ["d"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "z" if_any ["z"] if_not ["pregnant", "topless", "naked"]
        group top auto variant "a_pregnant" if_all ["a", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "d_pregnant" if_all ["d", "pregnant"] if_not ["topless", "naked"]
        group top auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["topless", "naked"]


        group stockings auto variant "a" if_any ["a"]
        group stockings auto variant "b" if_any ["b"]
        group stockings auto variant "d" if_any ["d"]
        group stockings auto variant "z" if_all ["z"] if_not ["pregnant", "bottomless", "naked"]
        group stockings auto variant "z_pregnant" if_all ["z", "pregnant"] if_not ["bottomless", "naked"]


        group garterbelt auto variant "z" if_all ["z"] if_not ["pregnant"]
        group garterbelt auto variant "z_pregnant" if_all ["z", "pregnant"]


        group arms_outfits auto variant "d_arms01" if_all ["arms01", "d"] if_not ["arms02", "dominatrix"]
        group arms_outfits auto variant "d_arms02" if_all ["arms02", "d"] if_not ["arms01", "dominatrix"]


        group acc_arm auto variant "a" if_any ["a"]
        group acc_arm auto variant "b" if_any ["b"]
        group acc_arm auto variant "d" if_any ["d"]
        group acc_arm auto variant "z" if_any ["z"]


        group necklace auto variant "a" if_any ["a"] if_not ["collar"]
        group necklace auto variant "b" if_any ["b"] if_not ["collar"]
        group necklace auto variant "d" if_any ["d"] if_not ["collar"]


        group collar auto if_all ["collar"] if_any ["a", "b"]


        attribute leash null
        group leash auto if_any ["leash"]


        group acc_ears auto variant "a" if_any ["a"]
        group acc_ears auto variant "b" if_any ["b"]
        group acc_ears auto variant "d" if_any ["d"]


        group tattoo auto variant "a" if_any ["a"]
        group tattoo auto variant "b" if_any ["b"]
        group tattoo auto variant "d" if_any ["d"]


        group acc_head auto
        group acc_head auto variant "a" if_any ["a"]
        group acc_head auto variant "b" if_any ["b"]
        group acc_head auto variant "d" if_any ["d"]

        group acc_waist auto variant "z" if_any ["z"] if_not ["bottomless", "naked"]


        group fx auto variant "a" if_any ["a"]
        group fx auto variant "b" if_any ["b"]
        group fx auto variant "d" if_any ["d"]
        group fx auto variant "z" if_any ["z"]


        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "d" if_any ["d"]

    layeredimage doctor kiss:
        attribute_function Pickers([MCPicker])
        always:
            "doctor_kiss_bodies"

        attribute naked null
        attribute topless null


        group multiple auto variant mcpiercings
        group mcoutfits auto if_not ["naked", "topless"]

    layeredimage doctor fuck:
        always "doctor_fuck_bg"
        always "doctor_fuck_bodies"
        if hero.flags.haircut:
            "doctor_fuck_haircut"

    layeredimage breemc gloryhole:
        attribute_function Pickers([MCCGPicker], npc=mike)
        attribute breemc null
        attribute nomc null

        attribute mc_casual null

        always "breemc_gloryhole_bg"


        group multiple auto variant bg_cum      


        group multiple auto variant bg_dick     


        attribute breemc null
        attribute right null
        attribute left null
        group lowbody if_not "nomc":
            attribute right default
            attribute left

        group upbody if_not "nomc":
            attribute rightstand default
            attribute leftstand
            attribute leftblowjob
            attribute rightblowjob


        group pubes auto if_all ["mc_pubes"] if_not "nomc"


        group pregnancy auto if_all ["mc_pregnant"] if_not "nomc"


        group head if_not "nomc":
            attribute rightstand default
            attribute leftstand
            attribute leftblowjob
            attribute rightblowjob


        attribute mc_nohaircut null
        group haircut auto if_all ["mc_haircut"] if_not "nomc"


        group collar if_all ["mc_collar"] if_not "nomc":
            attribute rightstand default
            attribute leftstand
            attribute leftblowjob
            attribute rightblowjob


        attribute mc_ears null
        attribute mc_lips null
        attribute mc_tongue null
        group multiple auto variant piercings_left when left and not nomc
        group multiple auto variant piercings_right when right and not nomc
        group multiple auto variant piercings_leftblowjob when leftblowjob and not nomc
        group multiple auto variant piercings_rightblowjob when rightblowjob and not nomc
        group multiple auto variant piercings_leftstand when leftstand and not nomc
        group multiple auto variant piercings_rightstand when rightstand and not nomc
        group multiple auto variant piercings when not nomc


        group left auto:
            attribute leftman
            attribute futa
            attribute cumshot


        group right auto:
            attribute rightman
            attribute mike


        group rdick auto:
            attribute stand
            attribute bj


        always "breemc_gloryhole_mouth_leftblowjob" if_any ["leftblowjob"]


        attribute breast null
        always "breemc_gloryhole_arm_righthand_leftstand_breast" if_all ["leftstand", "breast"] if_not ["leftblowjob", "rightblowjob", "rightstand", "nomc"]
        always "breemc_gloryhole_arm_righthand_leftblowjob_breast" if_all ["leftblowjob"] if_not "nomc"
        always "breemc_gloryhole_arm_righthand_leftstand" if_all ["leftstand"] if_not ["breast", "nomc"]
        always "breemc_gloryhole_arm_righthand_rightstand" if_all ["rightstand"] if_not "nomc"
        always "breemc_gloryhole_arm_righthand_rightblowjob" if_all ["rightblowjob"] if_not "nomc"

        always "breemc_gloryhole_arm_lefthand_rightstand_breast" if_all ["rightstand", "breast"] if_not ["leftblowjob", "rightblowjob", "leftstand", "nomc"]
        always "breemc_gloryhole_arm_lefthand_rightblowjob_breast" if_all ["rightblowjob"] if_not "nomc"
        always "breemc_gloryhole_arm_lefthand_rightstand" if_all ["rightstand"] if_not ["breast", "nomc"]
        always "breemc_gloryhole_arm_lefthand_leftstand" if_all ["leftstand"] if_not "nomc"
        always "breemc_gloryhole_arm_lefthand_leftblowjob" if_all ["leftblowjob"] if_not "nomc"


        group multiple auto variant cum      


        always "breemc_gloryhole_forelight"


    layeredimage swallow food:
        attribute_function Pickers([MCCGPicker])

        attribute breemc null
        attribute mc_haircut
        attribute mc_nohaircut
        attribute mc_collar

        group piercings auto

        attribute naked null
        attribute topless null
        attribute karate null

        group mcoutfits auto if_not ["naked", "topless"]

        group eyes auto:
            attribute opened default

        group mouth auto:
            attribute normal default

        group hand_position:
            attribute shallow null default
            attribute medium null
            attribute deep null

        attribute banana null
        group hand auto variant "banana" if_any "banana"
        group sleeve_banana auto variant "mc_casual" if_all ["banana", "mc_casual"]

        attribute icecream null
        group hand auto variant "icecream" if_any "icecream"
        group sleeve_icecream auto variant "mc_casual" if_all ["icecream", "mc_casual"]

    layeredimage breemc bj:


        group bg auto:
            attribute alley default


        group dude auto:
            attribute scottie default


        attribute naked null
        group outfit auto if_not ["naked"]


        group hand auto
        group sleeve auto if_not ["naked"]


        group dicks:
            attribute handjob null default
            attribute blowjob null
        group dick auto variant "handjob" if_any ["handjob"]
        group dick auto variant "blowjob" if_any ["blowjob"]


        group arms:
            attribute base null default
            attribute tip null
        group arm auto
        group arm auto variant "handjob" if_any ["handjob"]
        group toparm auto if_not ["naked"]
        group toparm auto variant "handjob" if_any ["handjob"] if_not ["naked"]


        always "breemc_bj_legs"
        always "breemc_bj_bot" if_not ["naked"]


        group body auto
        group top auto if_not ["naked"]


        group headpushondick:
            attribute small null default
            attribute medium null
            attribute big null
        group head auto
        group head auto variant "blowjob" if_any ["blowjob"]
        group muggerhand auto variant "blowjob" if_all ["mugger", "blowjob"]


        attribute facecum if_any ["handjob"]
        attribute breath if_any ["handjob"]


        attribute cum null
        group cum auto if_any ["cum"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
