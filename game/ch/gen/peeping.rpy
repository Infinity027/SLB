init python:
    class BathPositionPicker(object):
        def __call__(self, attr):
            found_npcs = set()
            if "female" in attr:
                attr.add("bree")
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    if (hero.is_male and g.id != 'mike') or (hero.is_female and g.id != 'bree'):
                        found_npcs.add(a)
            
            if found_npcs:
                if hero.is_male:
                    if found_npcs & {"bree", "lexi", "samantha"}:
                        attr.add("pose01")
                    elif found_npcs & {"sasha", "minami"}:
                        attr.add("pose02")
                else:
                    if "mike" in found_npcs:
                        
                        
                        if found_npcs & {"lexi", "samantha"}:
                            attr.add("pose01")
                        elif found_npcs & {"sasha", "minami"}:
                            attr.add("pose02")
                        else:
                            attr.add("pose01")
            if enable_debug_picker:
                renpy.log(f"BathPositionPicker results: {attr}")
            return attr

init 1:
    layeredimage peeping:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, PubesPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        always:
            "peeping_bg"
        group girls auto
        group bb auto
        group collars auto
        group haircuts auto
        group pregnancy auto if_any "pregnant"
        group multiple auto variant piercings
        group multiple auto variant piercings_boobjob when boobjob
        group multiple auto variant piercings_noboobjob when not sasha_boobjob
        group pubes auto
        always:
            "peeping_fg"

    layeredimage peeping_bath:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, BathPositionPicker], append_npc_from_attributes=True)
        attribute male null
        attribute mike null
        attribute female null

        always:
            "peeping_bath_bg"

        always:
            "peeping_bath_bathtub"

        group multiple auto variant girls
        group bb auto

        group mike auto if_any ["mike", "male"]

        always:
            "peeping_bath_faucets"

        group multiple auto variant piercings
        group multiple auto variant piercings_boobjob when sasha_boobjob
        group multiple auto variant piercings_noboobjob when not sasha_boobjob

        group multiple auto variant haircuts

        group multiple auto variant collars

        always:
            "peeping_bath_fg"

    layeredimage peeping_shower:
        attribute_function MultiPickers([CollarPicker, PiercingsPicker, HaircutPicker, PregnancyPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)

        always:
            "peeping_shower_bg"

        group bggirls auto
        group bgpregnancy auto if_any "pregnant"
        group multiple auto variant bgpiercings
        group bghaircuts auto
        group bgcollars auto

        group fggirls auto
        group fghaircuts auto if_any ["sasha"]
        group fgpregnancy auto if_any "pregnant"
        group multiple auto variant fgpiercings
        group fgcollars auto
        group arms auto
        group fghaircuts auto if_any ["minami"]

        always:
            "peeping_shower_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
