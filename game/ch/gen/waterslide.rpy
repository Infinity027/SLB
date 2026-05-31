init python:
    class WaterslidePositionPicker(object):
        def __call__(self, attr):
            if hero.is_female:
                g = attr & set(p.id for p in Person.all())
                g = list(g)[0] if g else None
                if g in ["angela", "ayesha", "kylie", "lexi", "sasha"]:
                    attr.add("back")
                else:
                    attr.add("ahead")
                    attr.add(g + "normal")
            if enable_debug_picker:
                renpy.log(f"WaterslidePositionPicker results: {attr}")
            return attr

init 1:
    layeredimage waterslide:
        attribute_function MultiPickers([HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker, PubesPicker, MCCGPicker, WaterslidePositionPicker], add_simple_pregnant_attribute=True, append_npc_from_attributes=True, use_morgan_cg_outfits=True)

        attribute naked null

        always "waterslide_bg"

        group mcposition auto


        group breemcposition auto:
            attribute ahead null
            attribute back null
        group mcposition auto variant "back" if_any "back"

        group mccollars auto variant "back" if_any "back"
        group mchaircuts auto variant "back" if_any "back"

        group multiple auto variant mcpiercings_back when back

        group mcoutfits auto variant "back" if_any "back"
        group mcpregnant auto variant "back" if_any "back"
        group mcoutfits auto variant "back_pregnant" if_any "back"

        group shade auto
        group npc auto

        group pregnancies auto

        group boobjob auto:
            attribute sasha_noboobjob null

        group multiple auto variant piercings_hidden when naked

        group multiple auto variant piercings
        group piercings auto variant "noboobjob" if_all ["sasha_noboobjob", "naked"]
        group piercings auto variant "boobjob" if_all ["sasha_boobjob", "naked"]

        group outfits auto

        attribute pregnant null
        group outfits auto variant "pregnant" if_any "pregnant"

        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        group outfits auto variant "noboobjob" if_any "sasha_noboobjob"
        group outfits auto variant "boobjob" if_any "sasha_boobjob"

        group collars auto

        group haircuts auto

        group glasses auto

        attribute morgan_makeup


        group mcshade auto if_any "breemc"

        group mcposition auto variant "ahead" if_any "ahead"
        group mccollars auto variant "ahead" if_any "ahead"
        group mchaircuts auto variant "ahead" if_any "ahead"

        group multiple auto variant mcpiercings_ahead_hidden when naked and breemc and ahead

        group multiple auto variant mcpiercings_ahead when ahead

        group mcoutfits auto variant "ahead" if_any "ahead"
        group mcpregnant auto variant "ahead" if_any "ahead"
        group mcoutfits auto variant "ahead_pregnant" if_any "ahead"

        group legs auto
        group mclegs auto
        group mclegs auto variant "back" if_any "back"

        always "waterslide_fg"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
