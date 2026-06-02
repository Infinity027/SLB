init 1:
    layeredimage drink:

        attribute_function MultiPickers([RoomPicker, HaircutPicker, CollarPicker, PregnancyPicker, PiercingsPicker, OutfitPicker], add_simple_pregnant_attribute=True, use_morgan_cg_outfits=True, append_npc_from_attributes=True)

        attribute nonpc null

        attribute casual null
        attribute date null
        attribute sexydate null
        attribute sluttydate null

        attribute necklace null

        attribute boobjob null
        attribute makeup null

        attribute glasses null
        attribute blazer null
        attribute smoke null

        group room auto:
            attribute club default
            attribute pub
            attribute nightclub null
            attribute stripclub null
            attribute vip null

        group people auto

        group multiple auto variant piercings_hidden

        group outfit auto

        group outfit auto variant "pregnant" if_any "pregnant"

        attribute sasha_boobjob null
        group outfit auto variant "bb" if_any "sasha_boobjob"

        group outfit auto variant "blazer" if_any "blazer"

        group collars auto

        group multiple auto variant piercings

        group ears_date auto if_any "ears_date"
        group ears_sexydate auto if_any "ears_sexydate"
        group eyebrow auto if_any "eyebrow"

        group glasses auto if_any "glasses"
        attribute reona_pureglasses

        group haircuts auto

        always "drink_hat_camila_sluttydate" if_all ["camila", "camila_sluttydate"]

        attribute morgan_makeup

        group table auto variant "club" if_any ["club", "stripclub", "nightclub", "vip"]
        group table auto variant "pub" if_any "pub"

        group room_fg auto if_not ["reona"]

        group arms auto
        group arms_outfit auto
        group drink auto
        group smoke auto
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
