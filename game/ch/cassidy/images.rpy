init 1:
    layeredimage cassidy:
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=cassidy)

        group veil auto variant "a" if_any ["a"]
        group veil auto variant "b" if_any ["b"]

        group position auto

        attribute blush null
        group blush auto if_any ["blush"]

        attribute facecum null
        group facecum auto if_any ["facecum"]

        attribute wet null
        group wet auto if_any ["wet"]

        attribute pubes null
        group pubes auto if_any ["pubes"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute ears null
        attribute nose null

        group acc_arm auto variant "a" if_any ["a"] if_not ["naked","topless"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["naked","topless"]

        group acc_neck auto variant "a" if_any ["a"] if_not ["collar"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["collar"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute naked null
        attribute gold null

        attribute bottomless null

        group stockings auto variant a when a and not (naked or bottomless)
        group stockings auto variant b when b and not (naked or bottomless)

        attribute topless null

        group chain auto variant "a" if_any ["a"] if_not ["collar"]
        group chain auto variant "b" if_any ["b"] if_not ["collar"]

        group acc auto variant a when a
        group acc auto variant b when b

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage cassidy close:
        yalign 0.16
        attribute_function Pickers([PositionPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=cassidy)

        group veil auto variant "a" if_any ["a"]
        group veil auto variant "b" if_any ["b"]

        group position auto

        attribute blush null
        group blush auto if_any ["blush"]

        attribute facecum null
        group facecum auto if_any ["facecum"]

        attribute wet null
        group wet auto if_any ["wet"]

        attribute pubes null
        group pubes auto if_any ["pubes"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default

        attribute ears null
        attribute nose null

        group acc_arm auto variant "a" if_any ["a"] if_not ["naked","topless"]
        group acc_arm auto variant "b" if_any ["b"] if_not ["naked","topless"]

        group acc_neck auto variant "a" if_any ["a"] if_not ["collar"]
        group acc_neck auto variant "b" if_any ["b"] if_not ["collar"]

        attribute collar null
        group collar auto if_any ["collar"]

        attribute naked null
        attribute gold null

        attribute bottomless null

        group stockings auto variant a when a and not (naked or bottomless)
        group stockings auto variant b when b and not (naked or bottomless)
 
        attribute topless null

        group chain auto variant "a" if_any ["a"] if_not ["collar"]
        group chain auto variant "b" if_any ["b"] if_not ["collar"]

        group acc auto variant a when a
        group acc auto variant b when b

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]

    layeredimage cassidy smartphone:
        always "cassidy_smartphone"

    layeredimage cassidy ending:
        attribute_function Pickers([ CollarPicker, EndingKidPicker], npc=cassidy)

        always "cassidy_ending_bg"

        attribute pregnant null

        attribute kid

        always "cassidy_ending_cassidy"

        attribute collar

        always "cassidy_ending_cassidy_casual"
        always "cassidy_ending_fx_cassidy"

        always "cassidy_ending_mike"
        always "cassidy_ending_mike_casual"
        always "cassidy_ending_fx_mike"

        always "cassidy_ending_fg"
