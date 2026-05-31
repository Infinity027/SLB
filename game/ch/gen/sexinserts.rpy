init 1:
    layeredimage sexinserts:
        attribute_function MultiPickers([HaircutPicker, PiercingsPicker, PubesPicker], append_npc_from_attributes=True)

        attribute chest null
        attribute bottom null
        attribute belly null
        attribute head null
        attribute sasha_boobjob null
        attribute cum null

        group unknown_attributes multiple:
            attribute lexi_ears null
            attribute lexi_nohaircut null
            attribute lexi_nose null

        group insert auto variant "belly" if_all ["belly"]
        group insert auto variant "bottom" if_all ["bottom"]
        group insert auto variant "chest" if_all ["chest"]
        group insert auto variant "chest_boobjob" if_all ["chest", "sasha_boobjob"]
        group insert auto variant "chest_noboobjob" if_all ["chest", "sasha"] if_not ["sasha_boobjob"]
        group insert auto variant "head" if_all ["head"]
        group haircuts_insert auto variant "bg" if_any "head"

        group insert_pubes auto if_any ["bottom"]

        group multiple auto variant add_piercing_insert_belly when belly
        group multiple auto variant add_piercing_insert_navel when belly
        group multiple auto variant add_piercing_insert_bottom when bottom
        group multiple auto variant add_piercing_insert_chest when chest
        group multiple auto variant add_piercing_insert_chest_boobjob when chest and sasha_boobjob
        group multiple auto variant add_piercing_insert_chest_noboobjob when chest and sasha and not sasha_boobjob
        group multiple auto variant add_piercing_insert_head when head

        group haircuts_insert auto if_any "head"
        group haircuts_insert auto variant "fg" if_any "head"

        group insert_cum auto variant "belly" if_all ["belly", "cum"]
        group insert_cum auto variant "bottom" if_all ["bottom", "cum"]
        group insert_cum auto variant "chest" if_all ["chest", "cum"]
        group insert_cum auto variant "chest_boobjob" if_all ["chest", "sasha_boobjob", "cum"]
        group insert_cum auto variant "chest_noboobjob" if_all ["chest", "cum", "sasha"] if_not ["sasha_boobjob"]
        group insert_cum auto variant "head" if_all ["head", "cum"]

    layeredimage pussy_insert:
        attribute_function MultiPickers([PiercingsPicker, PubesPicker], append_npc_from_attributes=True)

        attribute cum null

        group base auto
        group pubes auto
        group piercing auto
        group cum auto when cum

    layeredimage mouth_insert:
        attribute_function MultiPickers([HaircutPicker, PiercingsPicker], append_npc_from_attributes=True)

        attribute cum null

        group base auto

        group haircuts_insert auto
        group haircuts_insert auto variant "fg"

        group multiple auto variant piercing
        group cum auto when cum

    layeredimage belly_insert:
        attribute_function MultiPickers([PiercingsPicker], append_npc_from_attributes=True)

        attribute cum null

        group base auto
        group piercing auto
        group cum auto when cum

    layeredimage chest_insert:
        attribute_function MultiPickers([PiercingsPicker], append_npc_from_attributes=True)

        attribute sasha_boobjob null
        attribute sasha_noboobjob null
        attribute cum null

        group base auto
        group base auto variant "boobjob" if_any ["sasha_boobjob"]
        group base auto variant "noboobjob" if_all ["sasha"] if_not ["sasha_boobjob"]
        group piercing auto
        group piercing auto variant "boobjob" if_all ["sasha_boobjob", "piercing"]
        group piercing auto variant "noboobjob" if_all ["piercing", "sasha"] if_not ["sasha_boobjob"]
        group cum auto when cum
        group cum auto variant "boobjob" if_all ["sasha_boobjob", "cum"]
        group cum auto variant "noboobjob" if_all ["cum", "sasha"] if_not ["sasha_boobjob"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
