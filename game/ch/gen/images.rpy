init python:
    class MCCrossdressPicker(object):
        def __init__(self, id_prefix=False):
            self.id_prefix = id_prefix
        
        def __call__(self, attr):
            if game.flags.bandcrossdress and {'mike', 'mikemc'} & attr and "naked" not in attr:
                if self.id_prefix:
                    attr.add("mc_crossdress")
                    attr.discard("mc_casual")
                    attr.discard("mc_date")
                else:
                    attr.add("crossdress")
                    attr.discard("casual")
                    attr.discard("date")
            if enable_debug_picker:
                renpy.log(f"MCCrossdressPicker results: {attr}")
            return attr

    class ConcertPicker(object):
        def __init__(self, id_prefix=False):
            self.id_prefix = id_prefix
        
        def __call__(self, attr):
            if {'mike', 'mikemc'} & attr and not {"mc_hard", "hard", "mc_flaccid", "flaccid"} & attr:
                if hero.stamina and hero.is_male:
                    attr.add("mc_hard")
                    attr.add("hard")
                else:
                    attr.add("mc_flaccid")
                    attr.add("flaccid")
            if enable_debug_picker:
                renpy.log(f"ConcertPicker results: {attr}")
            return attr


screen continue_feedback():
    if renpy.showing("chibi"):
        frame:
            style "empty"
            align (0.76, 0.76)
            text "Click to continue" outlines [(2, "#00678b")]

init python:
    def animate_image(image_prefix, frames=60, fps=30, extension=''):
        animation_list=[]
        for i in range(frames):
            animation_list.append(f"{image_prefix}_{i}{extension}")    
            animation_list.append(1.0/fps)      
        return Animation(*animation_list)

init 1:
    layeredimage chibi:
        attribute_function Pickers([MCGenderPicker])
        attribute mikemc null
        attribute breemc null

        always:
            "chibi_bg"

        group mike auto if_any ["mikemc"]
        group bree auto if_any ["breemc"]

    layeredimage hand:
        always:
            "hand_hand"
        attribute bree:
            "hand_leash_bree"
        attribute sasha:
            "hand_leash_sasha"

    layeredimage 3dance:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker], append_npc_from_attributes=True)
        always:
            "3dance_mike"

        group multiple auto variant girl

        group multiple auto variant pregnancy
        group multiple auto variant collars
        group multiple auto variant haircuts
        attribute sasha_boobjob if_any["sasha"]
        always:
            if_all ["bree", "bree_pregnant"]
            "3dance_hand_bree_pregnant"
        always:
            if_all ["bree"]
            if_not ["bree_pregnant"]
            "3dance_hand_bree"
        always:
            if_all ["lexi", "lexi_pregnant"]
            "3dance_hand_lexi_pregnant"
        always:
            if_all ["lexi"]
            if_not ["lexi_pregnant"]
            "3dance_hand_lexi"

    image fx crow:
        contains:
            "gui/fx/crow/crow.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                linear 0.3 alpha 1.0
            parallel:
                linear 2 xalign 0.69 zoom 1.0
        contains:
            "gui/fx/crow/dot.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.56
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                pause 0.4
                linear 0.1 alpha 1.0
        contains:
            "gui/fx/crow/dot.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.59
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                pause 1.0
                linear 0.1 alpha 1.0
        contains:
            "gui/fx/crow/dot.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.62
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                pause 1.6
                linear 0.1 alpha 1.0
        pause 4.0
        linear 1.0 alpha 0.0

    image fx shock:
        contains:
            "gui/fx/shock.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.56
            yalign 0.15
            zoom 0.5
            alpha 0.0
            parallel:
                pause 0.1
                ease .04 yoffset -16 xoffset 16
                ease .04 yoffset 14 xoffset -14
                ease .03 yoffset -12 xoffset 12
                ease .03 yoffset 10 xoffset -10
                ease .02 yoffset -8 xoffset 8
                ease .02 yoffset 6 xoffset -6
                ease .01 yoffset -4 xoffset 4
                ease .01 yoffset 2 xoffset -2
                ease .01 yoffset 0 xoffset 0
            parallel:
                pause 2.0
                linear 0.05 zoom 0.4
                linear 0.05 zoom 0.5
                linear 0.05 zoom 0.4
                linear 0.05 zoom 0.5
            parallel:
                linear 0.05 alpha 1.0
                pause 2.1
                linear 0.1 alpha 0.0

    image fx sigh:
        contains:
            "gui/fx/sigh.png"
            xanchor 0.0
            yanchor 0.0
            xalign 0.55
            yalign 0.35
            zoom 0.0
            alpha 0.0
            parallel:
                ease 1.5 yoffset 30 xoffset 30
            parallel:
                linear 0.2 zoom 0.5
            parallel:
                linear 0.1 alpha 1.0
                pause 1.1
                linear 0.3 alpha 0.0

    image fx cough:
        contains:
            "gui/fx/sigh.png"
            xanchor 0.0
            yanchor 0.0
            xalign 0.55
            yalign 0.35
            zoom 0.0
            alpha 0.0
            parallel:
                ease 0.75 yoffset 15 xoffset 15
            parallel:
                linear 0.2 zoom 0.5
                linear 0.5 zoom 0.2
            parallel:
                linear 0.1 alpha 1.0
                pause 0.45
                linear 0.2 alpha 0.0

    image fx laugh:
        alpha 0.0
        contains:
            "gui/fx/laugh/laugh1.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.2
            zoom 0.8
            alpha 0.0
            parallel:
                linear 0.01 alpha 1.0
                pause 0.1
                linear 0.01 alpha 0.0
                pause 0.24
                repeat
        contains:
            "gui/fx/laugh/laugh2.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                pause 0.12
                linear 0.01 alpha 1.0
                pause 0.1
                linear 0.01 alpha 0.0
                pause 0.12
                repeat
        contains:
            "gui/fx/laugh/laugh3.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.2
            zoom 1.0
            alpha 0.0
            parallel:
                pause 0.24
                linear 0.01 alpha 1.0
                pause 0.1
                linear 0.01 alpha 0.0
                repeat
        parallel:
            linear 0.1 alpha 1.0
            pause 1.5
            linear 0.5 alpha 0.0

    image fx noise:
        contains:
            "gui/fx/noise.png"
            xanchor 0.0
            yanchor 0.5
            xalign 0.0
            yalign 0.5
            zoom 0.75
            alpha 0.0
            parallel:
                linear 0.05 alpha 1.0
                pause 0.1
                linear 0.1 alpha 0.0

    image fx heart:
        contains:
            "gui/fx/heart.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.55
            yalign 0.2
            zoom 0.25
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0 yalign 0.15
                linear 0.5 alpha 0.0 yalign 0.1
            parallel:
                linear 0.1 zoom 0.5
                linear 0.1 zoom 0.25
                linear 0.1 zoom 0.5
                linear 0.1 zoom 0.25
                linear 0.2 zoom 0.25
                linear 0.1 zoom 0.5
                linear 0.1 zoom 0.25
                linear 0.1 zoom 0.5
                linear 0.1 zoom 0.25

    image fx drop:
        contains:
            "gui/fx/drop.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.55
            yalign 0.2
            zoom 0.25
            alpha 0.0
            parallel:
                linear 1.0 alpha 1.0 yalign 0.25 zoom 0.5
                linear 1.0 alpha 0.0 yalign 0.3 zoom 0.25

    image fx fog = SnowBlossom("gui/fx/fog_particle.webp", count=80, border=600, xspeed=50, yspeed=0, start=5, fast=True, horizontal=True)

    image fx question:
        contains:
            "gui/fx/question.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.1
            zoom 0.5
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0 yalign 0.07 xalign 0.59 zoom 0.75
                linear 0.5 alpha 0.0 yalign 0.05 xalign 0.6 zoom 0.5

    image fx anger:
        contains:
            "gui/fx/anger.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.55
            yalign 0.2
            zoom 0.25
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
            parallel:
                linear 0.05 zoom 0.35
                linear 0.05 zoom 0.25
                repeat

    image fx exclamation:
        contains:
            "gui/fx/exclamation.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.1
            zoom 0.9
            alpha 0.0
            parallel:
                linear 0.5 alpha 1.0
                linear 0.5 alpha 0.0
            parallel:
                linear 0.05 zoom 1.0
                linear 0.05 zoom 0.9
                repeat

    image fx spirale:
        contains:
            "gui/fx/spirale.png"
            xanchor 0.5
            yanchor 0.5
            xalign 0.58
            yalign 0.1
            zoom 1.0
            alpha 1.0
            parallel:
                linear 2.5 rotate 360
                linear 0 rotate 0
                repeat

    transform impregnate_display(x, y):
        xalign x
        yalign y
        alpha 0.0
        linear 1.0 alpha 1.0
        2.5
        linear 1.0 alpha 0.0

    layeredimage arenabree:
        always:
            "arenabree_girl"

    layeredimage arenakat:
        always:
            "arenakat_girl"

    layeredimage arenatext:
        always:
            "arenatext_bree"
        always:
            "arenatext_kat"

    layeredimage arenabigtext:
        always:
            "arenafx_light"
        always:
            "arenabigtext_vs"


    layeredimage bar:
        always:
            "bar_background"
        always:
            "bar_man_back"
        always:
            "bar_foreground"

        always:
            "bar_man"
        always:
            "bar_light"

    layeredimage tv:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, OutfitPicker, HaircutPicker, MCCGPicker], append_npc_from_attributes=True)
        always:
            "tv_bg"

        attribute naked null


        attribute bree
        attribute bree_collar
        group multiple auto variant bree_piercings
        group bree_outfit auto if_not "naked"

        attribute breemc
        attribute mc_collar if_any "breemc"
        attribute mc_nohaircut null
        group multiple auto variant breemc_piercings when breemc
        group breemc_outfit auto if_any "breemc" if_not "naked"

        attribute mike
        attribute mikemc

        attribute sasha
        attribute sasha_boobjob
        attribute sasha_noboobjob null
        attribute sasha_collar
        attribute sasha_haircut
        attribute sasha_nohaircut null
        group multiple auto variant sasha_piercings
        group sasha_outfit auto if_not "naked"
        group sasha_outfit auto variant "boobjob" if_any "sasha_boobjob" if_not "naked"

    layeredimage blank:
        always:
            "blank_body"
        group outfit auto:
            attribute casual default
            attribute underwear null

    layeredimage blank close:
        yalign 0.04

        always:
            "blank_close_body"
        group outfit auto:
            attribute casual default
            attribute underwear null

    layeredimage concert:
        attribute_function MultiPickers([PubesPicker, CollarPicker, PiercingsPicker, OutfitPicker, PregnancyPicker, HaircutPicker, MCCGPicker, MCCrossdressPicker, ConcertPicker], append_npc_from_attributes=True, add_simple_outfit_attribute=True)
        attribute naked null
        attribute mc_hard null
        attribute mc_flaccid null
        attribute hard null
        attribute flaccid null
        attribute date null

        attribute amy_naked null
        attribute anna_naked null
        attribute kleio_naked null
        attribute sasha_naked null

        group kleio_tattoos:
            attribute kleio_angel null
            attribute kleio_wolf null

        group bg auto:
            attribute pub default

        attribute mikemc
        group mc_dick auto variant "flaccid" if_all ["mikemc", "mc_flaccid"]
        group mc_dick auto variant "hard" if_all ["mikemc", "mc_hard"]
        attribute mc_pubes if_any ["mikemc"]
        attribute mike
        group mike_dick auto variant "flaccid" if_all ["mike", "flaccid"]
        group mike_dick auto variant "hard" if_all ["mike", "hard"]


        group multiple auto variant npc
        group multiple auto variant pubes

        attribute anna_pregnant null
        attribute kleio_pregnant if_any ["kleio"]
        attribute sasha_pregnant if_any ["sasha"]

        group multiple auto variant piercings
        group multiple:
            attribute anna_clit null
            attribute anna_ears null
            attribute anna_tongue null
            attribute kleio_ears null
            attribute sasha_lips null
            attribute sasha_tongue null

        attribute sasha_noboobjob null
        attribute sasha_boobjob if_any ["sasha"]
        group multiple auto variant piercings_boobjob when boobjob

        group multiple auto variant outfits when not naked
        group outfits auto variant "boobjob" if_any "sasha_boobjob" if_not "naked"

        group outfits auto variant "anna_pregnant" if_any "anna_pregnant" if_not "naked"
        group outfits auto variant "kleio_pregnant" if_any "kleio_pregnant" if_not "naked"
        group outfits auto variant "sasha_pregnant" if_any "sasha_pregnant" if_not "naked"

        attribute sasha_haircut null
        attribute sasha_nohaircut null

        group multiple auto variant haircuts
        group multiple:
            attribute amy_nohaircut null
            attribute kleio_nohaircut null
            attribute anna_nohaircut null
        group haircuts auto variant "sasha_haircut" if_any "sasha_haircut"
        group haircuts auto variant "sasha_nohaircut" if_any "sasha_nohaircut"

        group multiple auto variant collars

        group mcoutfits auto if_not "naked"

        group multiple auto variant instruments
        group multiple auto variant instruments_naked when naked
        group multiple auto variant instruments_mc_naked when mc_naked

        group front_npc auto
        group front_pubes auto

        group front_outfits auto if_not "naked"

        group front_pregnancy auto

        group front_outfits auto variant "amy_pregnant" if_any "amy_pregnant" if_not "naked"

        group multiple auto variant front_piercings
        group multiple:
            attribute amy_clit null
            attribute amy_nipples null

        group front_collars auto

        group front_instruments auto

        group lights auto:
            attribute pub default

        always:
            "concert_fg"

    layeredimage concert solo:
        attribute_function Pickers([PubesPicker, PregnancyPicker, CollarPicker, HaircutPicker, OutfitPicker, PiercingsPicker, MCCrossdressPicker, DickPicker], clear_npc=True)

        group kleio_tattoos:
            attribute angel null
            attribute wolf null


        group bgs:
            attribute pub null default
            attribute stage null
            attribute nobg null
        group bg auto variant pub when pub and not nobg
        group bg auto variant stage when stage and not nobg



        group npc auto
        group mike auto when mike


        attribute pubes null
        group pubes auto when pubes



        attribute nipples null
        group nipples auto when nipples

        attribute clit null
        group clit auto when clit


        group outfits:
            attribute casual null default
            attribute date null
            attribute sexydate null
            attribute sluttydate null
            attribute naked null
        group outfit auto variant casual when casual and not naked
        group outfit auto variant date when date and not naked
        group outfit auto variant sexydate when sexydate and not naked
        group outfit auto variant sluttydate when sluttydate and not naked
        group mikeoutfit auto when mike


        attribute boobjob null
        group boobjob auto variant casual when boobjob and casual and not naked
        group boobjob auto variant date when boobjob and date and not naked
        group boobjob auto variant sexydate when boobjob and sexydate and not naked
        group boobjob auto variant sluttydate when boobjob and sluttydate and not naked
        group boobjob auto variant naked when boobjob and naked
        group nipples auto variant boobjob when nipples and boobjob and sasha and naked


        attribute haircut null
        attribute nohaircut null
        group haircut auto when haircut
        group nohaircut auto when nohaircut
        group mikehair auto when mike


        attribute pregnant null
        group pregnancies auto when pregnant

        group pregnant auto variant casual when pregnant and casual and not naked
        group pregnant auto variant date when pregnant and date and not naked
        group pregnant auto variant sexydate when pregnant and sexydate and not naked
        group pregnant auto variant sluttydate when pregnant and sluttydate and not naked



        attribute tongue null
        group tongue auto when tongue

        attribute nose null
        group nose auto when nose

        attribute ears null
        group ears auto when ears

        attribute navel null
        attribute pregnant_navel null
        group navel auto when navel
        group navel auto variant sexydate when navel and sexydate
        group pregnant_navel auto when pregnant_navel

        attribute lips null



        attribute collar null
        group collar auto when collar


        group instrument auto when not boobjob
        group instrument auto variant boobjob when boobjob


        attribute nobg null
        group light auto variant pub when pub and not nobg
        group light auto variant stage when stage and not nobg

    layeredimage rpg:
        attribute_function MultiPickers([PregnancyPicker, HaircutPicker, CollarPicker, PiercingsPicker, OutfitPicker], npcs=[bree, sasha], append_npc_from_attributes=True)

        attribute nojack null
        attribute nomc null
        attribute mikealone null
        attribute nosasha null
        attribute nobree null


        group bg auto:
            attribute livingroom default


        always "rpg_jack" if_any ["livingroom"] if_not ["nojack", "mikealone"]


        attribute minami if_not ["mikealone"]
        group exp_minami auto if_any ["minami"] if_not ["mikealone"]:
            attribute minaminormal default
        attribute minami_haircut if_any ["minami"] if_not ["mikealone"]
        attribute minami_nohaircut if_any ["minami"] if_not ["mikealone"]
        attribute minami_naked null
        group minamioutfits auto if_any ["minami"] if_not ["minami_naked", "mikealone"]
        group minamioutfits auto variant "haircut" if_all ["minami", "minami_haircut"] if_not ["minami_naked", "mikealone"]
        group minamioutfits auto variant "nohaircut" if_all ["minami", "minami_nohaircut"] if_not ["minami_naked", "mikealone"]
        attribute minami_pregnant if_all ["minami", "minami_naked"] if_not ["mikealone"]
        group minami_pregnant auto if_all ["minami", "minami_pregnant"] if_not ["minami_naked", "mikealone"]
        group minami_collar auto if_all ["minami", "minami_collar"] if_not ["mikealone"]
        group multiple auto variant minami_piercings when minami and not mikealone
        group multiple auto variant minami_piercings_naked when minami and minami_naked and not mikealone


        group mike auto if_not ["nomc"]


        always "rpg_sasha" if_not ["mikealone", "nosasha"]
        attribute sasha_haircut if_not ["mikealone", "nosasha"]
        attribute sasha_nohaircut if_not ["mikealone", "nosasha"]
        always "rpg_sasha_line" if_not ["mikealone", "nosasha"]
        group exp_sasha auto if_not ["mikealone", "nosasha"]:
            attribute sashanormal default null
        attribute sasha_naked null
        group sashaoutfits auto if_not ["sasha_naked", "mikealone", "nosasha"]
        attribute sasha_pregnant if_any ["sasha_naked"] if_not ["mikealone"]
        group sasha_pregnant auto if_any ["sasha_pregnant"] if_not ["sasha_naked", "mikealone", "nosasha"]
        attribute sasha_boobjob if_any ["sasha_naked"] if_not ["mikealone", "nosasha"]
        group sasha_boobjob auto if_any ["sasha_boobjob"] if_not ["sasha_naked", "mikealone", "nosasha"]
        attribute sasha_collar if_not ["mikealone", "nosasha"]
        group multiple auto variant sasha_piercings when not (mikealone or nosasha)
        group multiple auto variant sasha_piercings_naked when sasha_naked and not (mikealone or nosasha)
        group multiple auto variant sasha_piercings_naked_bb when sasha_naked and sasha_boobjob and not (mikealone or nosasha)
        group multiple auto variant sasha_piercings_naked_notbb when sasha_naked and not (sasha_boobjob or mikealone or nosasha)


        always "rpg_bree" if_not ["mikealone", "nobree"]
        group exp_bree auto if_not ["mikealone", "nobree"]:
            attribute breenormal default null
        attribute bree_naked null
        group breeoutfits auto if_not ["bree_naked", "mikealone", "nobree"]
        attribute bree_pregnant if_any ["bree_naked"] if_not ["mikealone", "nobree"]
        group bree_pregnant auto if_any ["bree_pregnant"] if_not ["bree_naked", "mikealone", "nobree"]
        attribute bree_collar if_not ["mikealone"]
        group multiple auto variant bree_piercings when not (mikealone or nobree)
        group multiple auto variant bree_piercings_breenormal when breenormal and not (mikealone or nobree)
        group multiple auto variant bree_piercings_naked when bree_naked and not (mikealone or nobree)
        group multiple auto variant bree_piercings_notliving when not (livingroom or mikealone or nobree)


        group table auto
        always "rpg_cup_sasha" if_any ["tavern"] if_not ["mikealone", "nosasha"]
        always "rpg_cup_bree" if_any ["tavern"] if_not ["mikealone", "nobree"]
        always "rpg_cup_minami" if_all ["tavern", "minami"] if_not ["mikealone"]
        always "rpg_minami_figure" if_all ["minami", "livingroom"] if_not ["mikealone"]



    layeredimage petplay:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PubesPicker, HaircutPicker, PiercingsPicker, DickPicker], append_npc_from_attributes=True)

        attribute bree null
        attribute cassidy null
        attribute hanna null
        attribute sasha null


        group arms auto:
            attribute nohold null default
            attribute hold null


        always:
            "petplay_bg"


        group bj auto:
            attribute breebj null
            attribute sashabj null
            attribute cassidybj null
            attribute hannabj null


        group mike auto if_not ["breebj", "sashabj", "cassidybj", "hannabj"]:
            attribute walk default
            attribute stand


        group mike auto variant "leftbj" if_any ["breebj", "hannabj"]
        group mike auto variant "rightbj" if_any ["sashabj", "cassidybj"]


        group breearm auto variant "nohold" if_all ["nohold", "bree", "stand"]
        group sashaarm auto variant "nohold" if_all ["nohold", "sasha", "stand"]
        group cassidyarm auto variant "nohold" if_all ["nohold", "cassidy", "stand"]
        group hannaarm auto variant "nohold" if_all ["nohold", "hanna", "stand"]


        group position auto variant "bree" if_any "bree":
            attribute walk
            attribute stand


        group position auto variant "sasha" if_any "sasha":
            attribute walk
            attribute stand


        group position auto variant "cassidy" if_any "cassidy":
            attribute walk
            attribute stand


        group position auto variant "hanna" if_any "hanna":
            attribute walk
            attribute stand


        attribute breepee if_any ["stand"]
        attribute sashapee if_any ["stand"]
        attribute cassidypee if_any ["stand"]
        attribute hannapee if_any ["stand"]


        group multiple auto variant pubic_walk when walk
        group multiple auto variant pubic_stand when stand


        group haircuts auto variant "walk" if_any ["walk"]
        group haircuts auto variant "stand" if_any ["stand"]


        group multiple auto variant piercings_behind_walk when walk


        group multiple auto variant pregnancy_walk when walk
        group multiple auto variant pregnancy_stand when stand


        group bb auto variant "walk" if_any ["walk"]



        group exp_bree auto variant "walk" if_all ["walk", "bree"]:
            attribute breenormal default
            attribute breehappy
        group exp_sasha auto variant "walk" if_all ["walk", "sasha"]:
            attribute sashanormal default
            attribute sashahappy
        group exp_cassidy auto variant "walk" if_all ["walk", "cassidy"]:
            attribute cassidynormal default
            attribute cassidyhappy
        group exp_hanna auto variant "walk" if_all ["walk", "hanna"]:
            attribute hannanormal default
            attribute hannahappy

        group eyes_bree auto if_all ["stand", "bree"]:
            attribute breeopeneyes default
            attribute breecloseeyes
        group eyes_sasha auto if_all ["stand", "sasha"]:
            attribute sashaopeneyes default
            attribute sashacloseeyes
        group eyes_cassidy auto if_all ["stand", "cassidy"]:
            attribute cassidyopeneyes default
            attribute cassidycloseeyes
        group eyes_hanna auto if_all ["stand", "hanna"]:
            attribute hannaopeneyes default
            attribute hannacloseeyes

        group mouth_bree auto if_all ["stand", "bree"] if_not ["inside"]:
            attribute breetongueout default
            attribute breeswallow
        group mouth_sasha auto if_all ["stand", "sasha"] if_not ["inside"]:
            attribute sashatongueout default
            attribute sashaswallow
        group mouth_cassidy auto if_all ["stand", "cassidy"] if_not ["inside"]:
            attribute cassidytongueout default
            attribute cassidyswallow
        group mouth_hanna auto if_all ["stand", "hanna"] if_not ["inside"]:
            attribute hannatongueout default
            attribute hannaswallow


        group multiple auto variant piercings_walk when walk
        group multiple auto variant piercings_stand when stand
        group multiple auto variant piercings_walk_notbb when walk and not sasha_boobjob
        group multiple auto variant piercings_walk_bb when walk and sasha_boobjob


        group multiple auto variant collars_walk when walk
        group multiple auto variant collars_stand when stand


        attribute cum null
        group multiple auto variant cum when cum 


        attribute leash default null
        group breeleash auto if_all ["bree_collar", "leash", "bree"] if_not ["breebj"]:
            attribute walk
            attribute stand
        group sashaleash auto if_all ["sasha_collar", "leash", "sasha"] if_not ["sashabj"]:
            attribute walk
            attribute stand
        group cassidyleash auto if_all ["cassidy_collar", "leash", "cassidy"] if_not ["cassidybj"]:
            attribute walk
            attribute stand
        group hannaleash auto if_all ["hanna_collar", "leash", "hanna"] if_not ["hannabj"]:
            attribute walk
            attribute stand

        group breeleash auto variant "breebj" if_all ["breebj", "bree_collar", "leash", "bree"]


        group mikedick auto:
            attribute inside null
            attribute outside null default

        group mikedicksize auto:
            attribute big null
            attribute medium null
            attribute small null

        group dick_inside auto variant "breebj" if_all ["inside", "breebj"]
        group dick_inside auto variant "sashabj" if_all ["inside", "sashabj"]
        group dick_inside auto variant "cassidybj" if_all ["inside", "cassidybj"]
        group dick_inside auto variant "hannabj" if_all ["inside", "hannabj"]

        group dick_outside_big auto variant "breebj" if_all ["outside", "breebj", "big"]
        group dick_outside_big auto variant "sashabj" if_all ["outside", "sashabj", "big"]
        group dick_outside_big auto variant "cassidybj" if_all ["outside", "cassidybj", "big"]
        group dick_outside_big auto variant "hannabj" if_all ["outside", "hannabj", "big"]

        group dick_outside_medium auto variant "breebj" if_all ["outside", "breebj", "medium"]
        group dick_outside_medium auto variant "sashabj" if_all ["outside", "sashabj", "medium"]
        group dick_outside_medium auto variant "cassidybj" if_all ["outside", "cassidybj", "medium"]
        group dick_outside_medium auto variant "hannabj" if_all ["outside", "hannabj", "medium"]

        group dick_outside_small auto variant "breebj" if_all ["outside", "breebj", "small"]
        group dick_outside_small auto variant "sashabj" if_all ["outside", "sashabj", "small"]
        group dick_outside_small auto variant "cassidybj" if_all ["outside", "cassidybj", "small"]
        group dick_outside_small auto variant "hannabj" if_all ["outside", "hannabj", "small"]


        attribute dickcum null
        group dickcum_outside_big auto variant "breebj" if_all ["dickcum", "outside", "breebj", "big"]
        group dickcum_outside_big auto variant "sashabj" if_all ["dickcum", "outside", "sashabj", "big"]
        group dickcum_outside_big auto variant "cassidybj" if_all ["dickcum", "outside", "cassidybj", "big"]
        group dickcum_outside_big auto variant "hannabj" if_all ["dickcum", "outside", "hannabj", "big"]

        group dickcum_outside_medium auto variant "breebj" if_all ["dickcum", "outside", "breebj", "medium"]
        group dickcum_outside_medium auto variant "sashabj" if_all ["dickcum", "outside", "sashabj", "medium"]
        group dickcum_outside_medium auto variant "cassidybj" if_all ["dickcum", "outside", "cassidybj", "medium"]
        group dickcum_outside_medium auto variant "hannabj" if_all ["dickcum", "outside", "hannabj", "medium"]

        group dickcum_outside_small auto variant "breebj" if_all ["dickcum", "outside", "breebj", "small"]
        group dickcum_outside_small auto variant "sashabj" if_all ["dickcum", "outside", "sashabj", "small"]
        group dickcum_outside_small auto variant "cassidybj" if_all ["dickcum", "outside", "cassidybj", "small"]
        group dickcum_outside_small auto variant "hannabj" if_all ["dickcum", "outside", "hannabj", "small"]


        attribute cumshot null
        group cumshot_inside auto variant "breebj" if_all ["cumshot", "inside", "breebj"]
        group cumshot_inside auto variant "sashabj" if_all ["cumshot", "inside", "sashabj"]
        group cumshot_inside auto variant "cassidybj" if_all ["cumshot", "inside", "cassidybj"]
        group cumshot_inside auto variant "hannabj" if_all ["cumshot", "inside", "hannabj"]

        group cumshot_outside_big auto variant "breebj" if_all ["cumshot", "outside", "breebj", "big"]
        group cumshot_outside_big auto variant "sashabj" if_all ["cumshot", "outside", "sashabj", "big"]
        group cumshot_outside_big auto variant "cassidybj" if_all ["cumshot", "outside", "cassidybj", "big"]
        group cumshot_outside_big auto variant "hannabj" if_all ["cumshot", "outside", "hannabj", "big"]

        group cumshot_outside_medium auto variant "breebj" if_all ["cumshot", "outside", "breebj", "medium"]
        group cumshot_outside_medium auto variant "sashabj" if_all ["cumshot", "outside", "sashabj", "medium"]
        group cumshot_outside_medium auto variant "cassidybj" if_all ["cumshot", "outside", "cassidybj", "medium"]
        group cumshot_outside_medium auto variant "hannabj" if_all ["cumshot", "outside", "hannabj", "medium"]

        group cumshot_outside_small auto variant "breebj" if_all ["cumshot", "outside", "breebj", "small"]
        group cumshot_outside_small auto variant "sashabj" if_all ["cumshot", "outside", "sashabj", "small"]
        group cumshot_outside_small auto variant "cassidybj" if_all ["cumshot", "outside", "cassidybj", "small"]
        group cumshot_outside_small auto variant "hannabj" if_all ["cumshot", "outside", "hannabj", "small"]


        group breearm auto variant "hold_breebj" if_all ["hold", "breebj"]
        group sashaarm auto variant "hold_sashabj" if_all ["hold", "sashabj"]
        group hannaarm auto variant "hold_hannabj" if_all ["hold", "hannabj"]
        group cassidyarm auto variant "hold_cassidybj" if_all ["hold", "cassidybj"]


        group bb auto variant "stand" if_any ["stand"]
        group multiple auto variant piercings_stand_notbb when stand and not sasha_boobjob
        group multiple auto variant piercings_stand_bb when stand and sasha_boobjob
        group sashaleash auto variant "sashabj" if_all ["sashabj", "sasha_collar", "leash"]


        always:
            "petplay_light"


    layeredimage new petplay:
        attribute_function MultiPickers([PregnancyPicker, CollarPicker, PubesPicker, PiercingsPicker], append_npc_from_attributes=True)


        group pose:
            attribute walk null default
            attribute pee null
            attribute back null


        always "new_petplay_bg_front" if_any ["walk", "pee"]
        always "new_petplay_bg_back" if_any ["back"]


        always "new_petplay_mike_front" if_any ["walk", "pee"]


        attribute leash_hanna "new_petplay_leash_hanna_front" if_all ["hanna", "hanna_collar"] if_any ["walk", "pee"]
        attribute leash_cassidy "new_petplay_leash_cassidy_front" if_all ["cassidy", "cassidy_collar"] if_any ["walk", "pee"]

        group left_girl:
            attribute hanna null
        group right_girl:
            attribute cassidy null
        group multiple auto variant girls_walk when walk
        group multiple auto variant girls_pee when pee
        group multiple auto variant girls_back when back


        group multiple auto variant pubes_walk when walk
        group multiple auto variant pubes_pee when pee
        group multiple auto variant pubes_back when back


        group multiple auto variant collars_walk when walk
        group multiple auto variant collars_pee when pee
        group multiple auto variant collars_back when back


        group multiple auto variant piercings_walk when walk
        group multiple auto variant piercings_pee when pee
        group multiple auto variant piercings_back when back


        group multiple auto variant pregnancy_walk when walk
        group multiple auto variant pregnancy_pee when pee
        group multiple auto variant pregnancy_back when back


        attribute leash_cassidy "new_petplay_leash_cassidy_back" if_all ["back", "cassidy", "cassidy_collar"]
        attribute leash_hanna "new_petplay_leash_hanna_back" if_all ["back", "hanna", "hanna_collar"]


        always "new_petplay_mike_back" if_any ["back"]

    layeredimage ryan natalie blowjob:


        always:
            "ryan_natalie_blowjob_ryan"


        group dick auto:
            attribute licking default

        attribute cumshot null
        group cumshot auto if_any "cumshot"


        group nat auto:
            attribute licking default


        group exp auto:
            if_any "licking"
            attribute normal default


        attribute cumtongue


        attribute facecum


        always:
            "ryan_natalie_blowjob_ryanoutfit"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
