init 1:
    layeredimage kleio:
        attribute_function Pickers([PositionPicker, HaircutPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=kleio)

        group position:
            attribute a null
            attribute b null
            attribute bbis null
            attribute c null
            attribute d null

        always:
            if_not ["c"]
            "kleio_body"
        always:
            if_any ["c"]
            if_not ["wolf", "angel"]
            "kleio_body_c"
        group tattoo auto variant "c" if_any "c"

        attribute pubes if_not ["c"]

        group tattoo auto variant "bot" if_not ["c"]

        attribute naked null
        group stockings auto if_not ["c", "bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null

        group chain auto if_not ["c", "bottomless", "naked"]

        attribute topless null

        attribute nojacket null
        group jacket auto if_not ["c", "nojacket", "topless", "naked"]
        group jacket auto variant "c" if_any ["c"] if_not ["nojacket", "topless", "naked"]

        group handpos:
            attribute a
            attribute b
            attribute bbis

        group top auto variant "arms_a" if_any ["a"] if_not ["topless", "naked"]
        group top auto variant "arms_b" if_any ["b"] if_not ["topless", "naked"]
        group top auto variant "arms_bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group top auto variant "arms_c" if_any ["c"] if_not ["topless", "naked"]

        group jacket auto variant "arms_a" if_any ["a"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_b" if_any ["b"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_bbis" if_any ["bbis"] if_not ["nojacket", "topless", "naked"]

        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]

        group tattoo auto variant "top_a" if_any ["a"]
        group tattoo auto variant "top_b" if_any ["b"]
        group tattoo auto variant "top_bbis" if_any ["bbis"]
        group tattoo auto variant "top_c" if_any ["c"]
        group tattoo auto variant "top_d" if_any ["d"]

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "bbis" if_any ["bbis"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default
        group exp auto variant "d" if_any ["d"]:
            attribute normal default

        attribute tongue null
        group googles auto if_not ["noacc", "topless", "naked"]

        group handpos:
            attribute d

        group top auto variant "arms_d" if_any ["d"] if_not ["topless", "naked"]

        group jacket auto variant "arms_d" if_any ["d"] if_not ["nojacket", "topless", "naked"]

        group gloves auto variant "d" if_any ["d"] if_not ["topless", "naked"]

        attribute noacc null
        group acc auto variant "hand_a" if_any ["a"] if_not ["noacc"]
        group acc auto variant "hand_b" if_any ["b"] if_not ["noacc"]
        group acc auto variant "hand_bbis" if_any ["bbis"] if_not ["noacc"]

        attribute mic if_any ["a", "bbis"] if_not ["noacc", "work", "halloween"]

        attribute collar null
        group collar auto if_any ["collar"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "bbis" if_any ["bbis"]
        group arm auto variant "c" if_any ["c"]
        group arm auto variant "d" if_any ["d"]

    layeredimage kleio close:
        yalign 0.25
        attribute_function Pickers([PositionPicker, HaircutPicker,  CollarPicker, PubesPicker, OutfitPicker], npc=kleio)
        group position:
            attribute a null
            attribute b null
            attribute bbis null
            attribute c null
            attribute d null

        always:
            if_not ["c"]
            "kleio_close_body"
        always:
            if_any ["c"]
            if_not ["wolf", "angel"]
            "kleio_close_body_c"
        group tattoo auto variant "c" if_any "c"

        attribute pubes if_not ["c"]

        group tattoo auto variant "bot" if_not ["c"]

        attribute naked null
        group stockings auto if_not ["c", "bottomless", "naked"]
        group stockings auto variant "c" if_any ["c"] if_not ["bottomless", "naked"]

        attribute bottomless null

        group chain auto if_not ["c", "bottomless", "naked"]

        attribute topless null

        attribute nojacket null
        group jacket auto if_not ["c", "nojacket", "topless", "naked"]
        group jacket auto variant "c" if_any ["c"] if_not ["nojacket", "topless", "naked"]

        group handpos:
            attribute a
            attribute b
            attribute bbis

        group top auto variant "arms_a" if_any ["a"] if_not ["topless", "naked"]
        group top auto variant "arms_b" if_any ["b"] if_not ["topless", "naked"]
        group top auto variant "arms_bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group top auto variant "arms_c" if_any ["c"] if_not ["topless", "naked"]

        group jacket auto variant "arms_a" if_any ["a"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_b" if_any ["b"] if_not ["nojacket", "topless", "naked"]
        group jacket auto variant "arms_bbis" if_any ["bbis"] if_not ["nojacket", "topless", "naked"]

        group gloves auto variant "a" if_any ["a"] if_not ["topless", "naked"]
        group gloves auto variant "b" if_any ["b"] if_not ["topless", "naked"]
        group gloves auto variant "bbis" if_any ["bbis"] if_not ["topless", "naked"]
        group gloves auto variant "c" if_any ["c"] if_not ["topless", "naked"]

        attribute haircut null
        attribute nohaircut null
        group haircut auto if_any ["haircut"]
        group nohaircut auto if_any ["nohaircut"]

        group tattoo auto variant "top_a" if_any ["a"]
        group tattoo auto variant "top_b" if_any ["b"]
        group tattoo auto variant "top_bbis" if_any ["bbis"]
        group tattoo auto variant "top_c" if_any ["c"]
        group tattoo auto variant "top_d" if_any ["d"]

        attribute blush null
        group blush auto if_any ["blush"]

        group exp auto variant "a" if_any ["a"]:
            attribute normal default
        group exp auto variant "b" if_any ["b"]:
            attribute normal default
        group exp auto variant "bbis" if_any ["bbis"]:
            attribute normal default
        group exp auto variant "c" if_any ["c"]:
            attribute normal default
        group exp auto variant "d" if_any ["d"]:
            attribute normal default

        attribute tongue null

        group googles auto if_not ["noacc", "topless", "naked"]

        group handpos:
            attribute d

        group top auto variant "arms_d" if_any ["d"] if_not ["topless", "naked"]

        group jacket auto variant "arms_d" if_any ["d"] if_not ["nojacket", "topless", "naked"]

        group gloves auto variant "d" if_any ["d"] if_not ["topless", "naked"]

        attribute noacc null
        group acc auto variant "hand_a" if_any ["a"] if_not ["noacc"]
        group acc auto variant "hand_b" if_any ["b"] if_not ["noacc"]
        group acc auto variant "hand_bbis" if_any ["bbis"] if_not ["noacc"]

        attribute mic if_any ["a", "bbis"] if_not ["noacc", "work", "halloween"]

        attribute collar null
        group collar auto if_any ["collar"]

        group arm auto variant "a" if_any ["a"]
        group arm auto variant "b" if_any ["b"]
        group arm auto variant "bbis" if_any ["bbis"]
        group arm auto variant "c" if_any ["c"]
        group arm auto variant "d" if_any ["d"]

    layeredimage kleio smartphone:
        always "kleio_smartphone"

    layeredimage kleio ending:
        attribute_function Pickers([CollarPicker,  OutfitPicker, EndingKidPicker], npc=kleio)

        always "kleio_ending_bg"
        always "kleio_ending_mike"

        always "kleio_ending_kleio"

        attribute collar

        group outfit auto

        attribute kid

        always "kleio_ending_fg"

    layeredimage kleio kart:
        attribute_function Pickers([CollarPicker,  HaircutPicker], npc=kleio)

        attribute bg null
        always "kleio_kart_bg" if_any ["bg"]

        attribute kleio null
        always "kleio_kart_kleionpc" if_any ["kleio"]

        attribute mike null
        always "kleio_kart_mikemc" if_any ["mike"]

        attribute collar

        group kleiohair auto if_any ["kleio"]

