init python:
    class GameArcadePositionPicker(object):
        def __call__(self, attr):
            
            for a in attr:
                g = Person.find(a)
                if g is not None:
                    break
            if g:
                if g.id in ["anna", "audrey", "bree", "hanna", "kleio", "lexi", "master", "mike", "minami", "sasha", "scottie", "shiori", "kat", "cherie", "claire", "kiara"]:
                    attr.add("pose01")
                elif g.id in ["alexis", "angela", "ayesha", "cassidy", "danny", "dwayne", "emma", "harmony", "jack", "lavish", "morgan", "ryan", "palla", "samantha", "reona"]:
                    attr.add("pose02")
                elif g.id in ["aletta", "camila", "shawn", "victor", "amy"]:
                    attr.add("pose03")
            
            
            if hero.is_male:
                attr.add("mikeMC")
            else:
                attr.add("breeMC")
            
            if enable_debug_picker:
                renpy.log(f"GameArcadePositionPicker results: {attr}")
            return attr

init 1:
    layeredimage game arcade:
        attribute_function MultiPickers([GameArcadePositionPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True)


        group bg auto


        attribute mikeMC null
        group mikemc auto if_any ["mikeMC"]
        attribute breeMC null
        group breemc auto if_any ["breeMC"]


        group girl auto


        attribute morgan_makeup


        group collars auto


        group pregnancy auto


        group bb auto



        group outfit_bot auto
        group outfit_bot auto variant "pregnant" if_any ["pregnant"]

        group outfit_top auto
        group outfit_top auto variant "pregnant" if_any ["pregnant"]


        group outfits auto
        group outfits auto variant "pregnant" if_any ["pregnant"]


        group haircuts auto


        group multiple auto variant piercings_hidden when not reona_purecasual
        group multiple auto variant piercings_hidden_haircut when camila_haircut and not reona_purecasual


        group multiple auto variant piercings
        group multiple auto variant piercings_haircut when haircut


        group acc


        group fg auto


        group title auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
