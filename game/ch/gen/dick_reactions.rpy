init python:
    class CG_DickReactions_Picker(object):
        def __call__(self, attr):
            if attr & {"ryan"}:
                attr.add("vsmall")
            elif attr & {"jack", "shawn"}:
                attr.add("small")
            elif attr & {"master", "danny"}:
                attr.add("medium")
            elif attr & {"scottie", "victor"}:
                attr.add("big")
            elif attr & {"dwayne"}:
                attr.add("vbig")
            
            if enable_debug_picker:
                renpy.log(f"CG_DickReactions_Picker results: {attr}")
            return attr

init 1:
    layeredimage dick reactions:
        attribute_function Pickers([PiercingsPicker, HaircutPicker, CollarPicker, MCCGPicker, CG_DickReactions_Picker], clear_npc=True)

        attribute mikemc null

        attribute haircut null
        attribute nohaircut null

        attribute clit null
        attribute navel null
        attribute pregnant_navel null
        attribute nipples null


        attribute nobreemc null
        group npc auto
        attribute breemc if_not ["nobreemc"]


        group haircut auto when haircut and (camila or minami or sasha)
        group nohaircut auto when nohaircut and (camila or minami or sasha)
        attribute mc_haircut if_any ["breemc"] if_not ["nobreemc"]


        group exp:
            attribute smile null default
            attribute mock null
            attribute tasty null
            attribute scared null
            attribute disgusted null
        group smile auto if_any ["smile"]:
            attribute breemc if_not ["nobreemc"]
        group mock auto if_any ["mock"]:
            attribute breemc if_not ["nobreemc"]
        group tasty auto if_any ["tasty"]:
            attribute breemc if_not ["nobreemc"]
        group scared auto if_any ["scared"]:
            attribute breemc if_not ["nobreemc"]
        group disgusted auto if_any ["disgusted"]:
            attribute breemc if_not ["nobreemc"]


        group makeup auto variant "smile" if_all ["makeup", "smile"]
        group makeup auto variant "mock" if_all ["makeup", "mock"]
        group makeup auto variant "tasty" if_all ["makeup", "tasty"]
        group makeup auto variant "scared" if_all ["makeup", "scared"]
        group makeup auto variant "disgusted" if_all ["makeup", "disgusted"]



        attribute lips null
        group lips auto variant "smile" if_all ["lips", "smile"]
        group lips auto variant "mock" if_all ["lips", "mock"]
        group lips auto variant "tasty" if_all ["lips", "tasty"]
        group lips auto variant "scared" if_all ["lips", "scared"]
        group lips auto variant "disgusted" if_all ["lips", "disgusted"]
        group mc_lips auto if_any ["breemc"] if_not ["nobreemc"]

        attribute tongue null
        group tongue auto variant "smile" if_all ["tongue", "smile"]
        group tongue auto variant "mock" if_all ["tongue", "mock"]
        group tongue auto variant "tasty" if_all ["tongue", "tasty"]
        group tongue auto variant "scared" if_all ["tongue", "scared"]
        group tongue auto variant "disgusted" if_all ["tongue", "disgusted"]
        group mc_tongue auto if_any ["breemc"] if_not ["nobreemc"]

        attribute nose null
        group nose auto variant "smile" if_all ["nose", "smile"]
        group nose auto variant "mock" if_all ["nose", "mock"]
        group nose auto variant "tasty" if_all ["nose", "tasty"]
        group nose auto variant "scared" if_all ["nose", "scared"]
        group nose auto variant "disgusted" if_all ["nose", "disgusted"]
        group mc_nose auto if_any ["breemc"] if_not ["nobreemc"]

        attribute ears null
        group ears auto variant "smile" if_all ["ears", "smile"]
        group ears auto variant "mock" if_all ["ears", "mock"]
        group ears auto variant "tasty" if_all ["ears", "tasty"]
        group ears auto variant "scared" if_all ["ears", "scared"]
        group ears auto variant "disgusted" if_all ["ears", "disgusted"]
        group mc_ears auto if_any ["breemc"] if_not ["nobreemc"]

        attribute eyebrow null
        group eyebrow auto variant "smile" if_all ["eyebrow", "smile"]
        group eyebrow auto variant "mock" if_all ["eyebrow", "mock"]
        group eyebrow auto variant "tasty" if_all ["eyebrow", "tasty"]
        group eyebrow auto variant "scared" if_all ["eyebrow", "scared"]
        group eyebrow auto variant "disgusted" if_all ["eyebrow", "disgusted"]
        group mc_eyebrow auto if_any ["breemc"] if_not ["nobreemc"]


        attribute collar null
        group collar auto if_any ["collar"]
        attribute mc_collar if_any ["breemc"] if_not ["nobreemc"]


        group haircut auto if_all ["haircut"] if_any ["aletta"]
        group nohaircut auto if_all ["nohaircut"] if_any ["aletta"]



        attribute lips null
        group lips auto if_any ["lips"]
        attribute mc_lips if_any ["breemc"] if_not ["nobreemc"]

        attribute tongue null
        group tongue auto if_any ["tongue"]
        attribute mc_tongue if_any ["breemc"] if_not ["nobreemc"]

        attribute nose null
        group nose auto if_any ["nose"]
        attribute mc_nose if_any ["breemc"] if_not ["nobreemc"]

        attribute ears null
        group ears auto if_any ["ears"]
        attribute mc_ears if_any ["breemc"] if_not ["nobreemc"]

        attribute eyebrow null
        group eyebrow auto if_any ["eyebrow"]
        attribute mc_eyebrow if_any ["breemc"] if_not ["nobreemc"]


        group haircut auto when haircut and (kleio or morgan or reona or cherie or claire or kiara)
        group nohaircut auto when nohaircut and (kleio or morgan or reona or cherie or claire or kiara)


        attribute nodick null
        group dick auto if_not ["nodick"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
