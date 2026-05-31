init 1:
    layeredimage spank:
        attribute_function Pickers([OutfitPicker, CollarPicker, PiercingsPicker, PregnancyPicker], clear_npc=True)

        attribute pregnant
        attribute clit null
        attribute naked null
        attribute collar null





        group bg auto variant "aletta" if_any "aletta":
            attribute personal default
        group bg auto variant "audrey" if_any "audrey":
            attribute personal default
        group bg auto variant "lavish" if_any "lavish":
            attribute personal default
        group bg auto variant "shiori" if_any "shiori":
            attribute personal default

        group mike auto

        always:
            if_all ["aletta"]
            if_any ["work", "sexywork"]
            if_not "naked"
            "spank_mike_outfit_aletta_work"
        always:
            if_all ["audrey"]
            if_any ["work", "sexywork"]
            if_not "naked"
            "spank_mike_outfit_audrey_work"
        always:
            if_all ["lavish"]
            if_any ["work", "sexywork"]
            if_not "naked"
            "spank_mike_outfit_lavish_work"
        always:
            if_all ["shiori"]
            if_any ["work", "sexywork"]
            if_not "naked"
            "spank_mike_outfit_shiori_work"

        group girl auto

        group pregnant auto if_any "pregnant"

        group exp auto variant "audrey" if_any "audrey":
            attribute normal default
        group exp auto variant "aletta" if_any "aletta":
            attribute normal default
        group exp auto variant "lavish" if_any "lavish":
            attribute normal default
        group exp auto variant "shiori" if_any "shiori":
            attribute normal default

        group multiple auto variant piercings_aletta when aletta
        group multiple auto variant piercings_audrey when audrey
        group multiple auto variant piercings_lavish when lavish
        group multiple auto variant piercings_shiori when shiori

        group fx auto variant "aletta" if_any ["aletta"]
        group fx auto variant "audrey" if_any ["audrey"]
        group fx auto variant "lavish" if_any ["lavish"]
        group fx auto variant "shiori" if_any ["shiori"]

        group multiple auto variant outfit_aletta when aletta and not naked

        group multiple auto variant outfit_aletta_pregnant when aletta and pregnant and not naked

        group multiple auto variant outfit_audrey when audrey and not naked

        group multiple auto variant outfit_audrey_pregnant when audrey and pregnant and not naked

        group top auto variant "audrey" if_any "audrey" if_not "naked"
        group top auto variant "audrey_pregnant" if_all ["audrey","pregnant"] if_not "naked"

        attribute pulled null
        group bot auto variant "audrey" if_any "audrey" if_not ["naked", "pulled"]
        group bot auto variant "audrey_pulled" if_all ["audrey", "pulled"] if_not "naked"


        group multiple auto variant outfit_lavish when lavish and not naked

        group multiple auto variant outfit_lavish_pregnant when lavish and pregnant and not naked

        group multiple auto variant outfit_shiori when shiori and not naked

        group multiple auto variant outfit_shiori_pregnant when shiori and pregnant and not naked

        group collar auto if_any "collar"

        group mike_arm_positions auto:
            attribute ready null default
            attribute spank null
            attribute up null
            attribute fingerpussy null
            attribute fingerass null

        group mike_arm auto variant "aletta" if_any ["aletta"]
        group mike_arm_outfit auto variant "aletta_work" if_all ["aletta"] if_any ["work", "sexywork"] if_not "naked"

        group mike_arm auto variant "audrey" if_any ["audrey"]
        group mike_arm_outfit auto variant "audrey_work" if_all ["audrey"] if_any ["work", "sexywork"] if_not "naked"

        group mike_arm auto variant "lavish" if_any ["lavish"]
        group mike_arm_outfit auto variant "lavish_work" if_all ["lavish"] if_any ["work", "sexywork"] if_not "naked"

        group mike_arm auto variant "shiori" if_any ["shiori"]
        group mike_arm_outfit auto variant "shiori_work" if_all ["shiori"] if_any ["work", "sexywork"] if_not "naked"

        group multiple auto variant outfit_audrey_fingerpussy when audrey and fingerpussy and not naked
        group multiple auto variant outfit_audrey_fingerass when audrey and fingerass and not naked

        group multiple auto variant bot_audrey_fingerpussy when audrey and fingerpussy and not (naked or pulled)
        group multiple auto variant bot_audrey_fingerass when audrey and fingerass and not (naked or pulled)

        always:
            if_all ["aletta"]
            if_any ["work", "sexywork"]
            if_not "naked"
            "spank_glasses_aletta_work"

        group fg auto variant "aletta" if_any ["aletta"]
        group fg auto variant "audrey" if_any ["audrey"]
        group fg auto variant "lavish" if_any ["lavish"]
        group fg auto variant "shiori" if_any ["shiori"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
