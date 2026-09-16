init 1:
    layeredimage reona:
        attribute_function Pickers([ PubesPicker, CollarPicker, OutfitPicker], npc=reona)

        attribute idle null

        group wings auto
        group tail auto

        group lefthand if_not ["rpg"]:
            attribute leftback
        attribute wallet if_any ["leftback"] if_not ["rpg"]

        group backhaircuts auto
        always "reona_body" if_not "halloween"
        always "reona_halloween_body" if_any "halloween"

        group haircuts auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute collar if_not ["rpg"]

        attribute blush

        group exp auto:
            attribute normal default
        attribute saliva if_all ["lick", "leftnormal"] if_not ["mask"]

        attribute ears null
        attribute tongue null

        attribute mask if_not ["rpg"]

        group lefthand auto if_not ["leftback", "rpg"]:
            attribute leftnormal default
        group righthand auto if_not ["rpg"]:
            attribute rightnormal default null
        group righthand auto variant "haircut" if_any ["haircut"] if_not ["rpg"]
        group righthand auto variant "nohaircut" if_any ["nohaircut"] if_not ["rpg"]

        group multiple:
            attribute tongue null

        attribute innersexy null
        attribute bottomless null
        attribute topless null
        attribute naked null
        attribute nojacket null
        group multiple auto variant sleeve_back_halloween when halloween and not (topless or naked)
        group multiple auto variant sleeve_back_date when date and not (topless or naked)       
        group multiple auto variant sleeve_casual when casual and not (topless or naked)
        group multiple auto variant sleeve_date when date and not (topless or naked)

        group necklace auto if_not ["collar"]

        attribute noacc null
        group multiple auto variant acc_hand_casual when casual and not noacc
        group multiple auto variant acc_hand_date when date and not noacc
        group multiple auto variant acc_hand_sexydate when sexydate and not noacc
        group acc_head auto if_not ["noacc"]
        attribute glasses if_not ["rpg"]
        attribute pureglasses if_not ["rpg"]
        attribute dildo if_any ["righthold"] if_not ["rpg"]

        always "reona_hands_rpg" if_any ["rpg"]

        group arm auto

    layeredimage reona close:
        yalign 0.2
        attribute_function Pickers([ PubesPicker, CollarPicker, OutfitPicker], npc=reona)

        attribute idle null

        group wings auto
        group tail auto

        group lefthand if_not ["rpg"]:
            attribute leftback
        attribute wallet if_any ["leftback"] if_not ["rpg"]

        group backhaircuts auto
        always "reona_close_body" if_not "halloween"
        always "reona_close_halloween_body" if_any "halloween"

        group haircuts auto

        attribute pubes null
        group pubes auto if_any "pubes"

        attribute collar if_not ["rpg"]

        attribute blush

        group exp auto:
            attribute normal default
        attribute saliva if_all ["lick", "leftnormal"] if_not ["mask"]

        attribute ears null
        attribute tongue null

        attribute mask if_not ["rpg"]

        group lefthand auto if_not ["leftback", "rpg"]:
            attribute leftnormal default
        group righthand auto if_not ["rpg"]:
            attribute rightnormal default null
        group righthand auto variant "haircut" if_any ["haircut"] if_not ["rpg"]
        group righthand auto variant "nohaircut" if_any ["nohaircut"] if_not ["rpg"]

        group multiple:
            attribute tongue null

        attribute innersexy null
        attribute bottomless null
        attribute topless null
        attribute naked null
        attribute nojacket null
        group multiple auto variant sleeve_back_halloween when halloween and not (topless or naked)
        group multiple auto variant sleeve_back_date when date and not (topless or naked)
        group multiple auto variant sleeve_casual when casual and not (topless or naked)
        group multiple auto variant sleeve_date when date and not (topless or naked)

        group necklace auto if_not ["collar"]

        attribute noacc null
        group multiple auto variant acc_hand_casual when casual and not noacc
        group multiple auto variant acc_hand_date when date and not noacc
        group multiple auto variant acc_hand_sexydate when sexydate and not noacc
        group acc_head auto if_not ["noacc"]
        attribute glasses if_not ["rpg"]
        attribute pureglasses if_not ["rpg"]
        attribute dildo if_any ["righthold"] if_not ["rpg"]

        always "reona_close_hands_rpg" if_any ["rpg"]

        group arm auto
