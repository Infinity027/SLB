init 1:
    layeredimage violaine:
        attribute_function Pickers([PositionPicker, PubesPicker,  CollarPicker, OutfitPicker], npc=violaine)


        attribute naked null
        attribute topless null
        attribute bottomless null
        attribute nopatsies null

        group wings auto variant a when a and not (naked or topless)
        group wings auto variant b when b and not (naked or topless)

        group position auto
        group tattoo auto

        attribute pubes null
        group pubes auto when pubes


        attribute pregnant null
        group pregnancy auto when pregnant:
            attribute b when naked or not (sport or sluttydate)


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default

        group wig auto when halloween

        group patsies auto variant a when a and not (naked or topless or nopatsies)
        group patsies auto variant b when b and not (naked or topless or nopatsies)

        group bot_a auto variant preg when a and not (naked or bottomless)
        group bot_b auto variant preg when b and not (naked or bottomless)


        group belly auto variant b when b and not naked

        group top_a auto when a and not (naked or topless)
        group top_b auto when b and not (naked or topless)
        group top_a auto variant preg when a and not (naked or topless)
        group top_b auto variant preg when b and not (naked or topless)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar


        group collar auto when collar


        group acc_head auto variant a when a and not (naked or topless)
        group acc_head auto variant b when b and not (naked or topless)

    layeredimage violaine close:
        yalign 0.12
        attribute_function Pickers([PositionPicker, PubesPicker,  CollarPicker, OutfitPicker], npc=violaine)


        attribute naked null
        attribute topless null
        attribute bottomless null
        attribute nopatsies null

        group wings auto variant a when a and not (naked or topless)
        group wings auto variant b when b and not (naked or topless)

        group position auto
        group tattoo auto

        group pubes auto when pubes


        group pregnancy auto when pregnant:
            attribute b when naked or not (sport or sluttydate)


        group exp auto variant a when a:
            attribute normal default
        group exp auto variant b when b:
            attribute normal default

        group wig auto when halloween

        group patsies auto variant a when a and not (naked or topless or nopatsies)
        group patsies auto variant b when b and not (naked or topless or nopatsies)

        group bot_a auto when a and not (naked or bottomless)
        group bot_b auto when b and not (naked or bottomless)
        group bot_a auto variant preg when a and not (naked or bottomless)
        group bot_b auto variant preg when b and not (naked or bottomless)


        group belly auto variant b when b and not naked
        always "violaine_close_piercings_b_pregnant_navel" when b and pregnant_navel and not naked and (sport or sluttydate)


        group top_a auto when a and not (naked or topless)
        group top_b auto when b and not (naked or topless)
        group top_a auto variant preg when a and not (naked or topless)
        group top_b auto variant preg when b and not (naked or topless)


        group necklace auto variant a when a and not collar
        group necklace auto variant b when b and not collar


        group collar auto when collar


        group acc_head auto variant a when a and not (naked or topless)
        group acc_head auto variant b when b and not (naked or topless)

    layeredimage violaine smartphone:
        always "violaine_smartphone"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
