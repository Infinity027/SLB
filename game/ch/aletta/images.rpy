init 1:
    # ── ALETTA - Main standing character images ─────────────────────────────────
    # Path: ch/images/aletta/<outfit>/<expression>.webp
    # Outfits: casual, casual_b, work, date, nude, special_event, home_hotcoffee

    # # --- Casual outfit (default / a-variant) ---
    # image aletta             = "ch/images/aletta/casual/normal.webp"
    # image aletta normal      = "ch/images/aletta/casual/normal.webp"
    # image aletta happy       = "ch/images/aletta/casual/happy.webp"
    # image aletta sad         = "ch/images/aletta/casual/sad.webp"
    # image aletta angry       = "ch/images/aletta/casual/angry.webp"
    # image aletta flirt       = "ch/images/aletta/casual/flirt.webp"
    # image aletta blush       = "ch/images/aletta/casual/blush.webp"
    # image aletta surprised   = "ch/images/aletta/casual/surprised.webp"
    # image aletta talk   = "ch/images/aletta/casual/talk.webp"
    # image aletta dreamy      = "ch/images/aletta/casual/dreamy.webp"
    # image aletta pain        = "ch/images/aletta/casual/pain.webp"
    # image aletta whining     = "ch/images/aletta/casual/whining.webp"
    # image aletta sadsmile    = "ch/images/aletta/casual/sadsmile.webp"
    # image aletta wink        = "ch/images/aletta/casual/wink.webp"
    # image aletta annoyed     = "ch/images/aletta/casual/annoyed.webp"
    # image aletta upset       = "ch/images/aletta/casual/upset.webp"
    # image aletta embarrassed = "ch/images/aletta/casual/embarrassed.webp"
    # image aletta stuned      = "ch/images/aletta/casual/stunned.webp"
    # image aletta normal blush = "ch/images/aletta/casual/blush.webp"

    # # --- Casual "b" outfit variant ---
    # image aletta b           = "ch/images/aletta/casual_b/normal.webp"
    # image aletta b flirt     = "ch/images/aletta/casual_b/flirt.webp"
    # image aletta b underwear = "ch/images/aletta/casual_b/underwear.webp"
    # image aletta normal b underwear = "ch/images/aletta/casual_b/underwear.webp"

    # # --- Date outfit ---
    # image aletta date normal = "ch/images/aletta/date/normal.webp"
    # image aletta date happy  = "ch/images/aletta/date/happy.webp"

    # # --- Underwear ---
    # image aletta underwear   = "ch/images/aletta/casual/underwear.webp"

    # # --- Nude ---
    # image aletta naked        = "ch/images/aletta/nude/normal.webp"
    # image aletta naked angry  = "ch/images/aletta/nude/angry.webp"
    # image aletta naked blush  = "ch/images/aletta/nude/blush.webp"
    # image aletta b naked      = "ch/images/aletta/nude/normal.webp"
    # image aletta blush b naked = "ch/images/aletta/nude/blush.webp"

    # # --- Halloween special outfit ---
    # image aletta halloween           = "ch/images/aletta/special_event/halloween.webp"
    # image aletta halloween talkative = "ch/images/aletta/special_event/halloween_talkative.webp"
    # image aletta halloween flirt     = "ch/images/aletta/special_event/halloween_flirt.webp"

    # # ── ALETTA CLOSE-UP ─────────────────────────────────────────────────────────
    # # Used for intimate/indoor scenes
    # # Path: ch/images/aletta/<outfit>/close_<expression>.webp
    # image aletta close         = "ch/images/aletta/casual/close_normal.webp"
    # image aletta close b naked = "ch/images/aletta/nude/close_normal.webp"

    layeredimage aletta smartphone:
        always "aletta_smartphone"

    layeredimage aletta vibrator:

        attribute nobg null
        attribute noshiori null
        attribute noglasses null

        always "aletta_vibrator_bg" if_not ["nobg"]

        always "aletta_vibrator_shiori" if_not ["noshiori"]

        always "aletta_vibrator_aletta"

        group exp auto:
            attribute embarrassed default

        group shiori_exp auto:
            attribute shiori_worried default

        group location auto:
            attribute inside default
            attribute novibrator null

        attribute open if_not ["inside"]

        attribute squirt if_not ["inside"]

        attribute on if_any ["inside"]
        attribute blurry if_any ["fall"]

        always "aletta_vibrator_glasses" if_not ["noglasses"]

    layeredimage aletta ropeplay:
        attribute_function Pickers([CollarPicker, PubesPicker, OutfitPicker], npc=aletta)

        always "aletta_ropeplay_bg"

        group position auto:
            attribute a default

        group pubes auto variant "a" if_all ["a", "pubes"]
        group pubes auto variant "b" if_all ["b", "pubes"]

        group exp auto:
            attribute normal default

        attribute blindfold

        always "aletta_ropeplay_glasses" if_not ["blindfold"]

        attribute gag

        attribute chain

        attribute nopanties null
        group panties auto variant "a" if_any ["a"] if_not ["nopanties", "naked"]
        group panties auto variant "b" if_any ["b"] if_not ["pregnant", "nopanties", "naked"]
        group panties auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["nopanties", "naked"]

        attribute bottomless null
        group bot auto variant "a" if_any ["a"] if_not ["bottomless", "naked"]
        group bot auto variant "b" if_any ["b"] if_not ["pregnant", "bottomless", "naked"]
        group bot auto variant "b_pregnant" if_all ["b", "pregnant"] if_not ["bottomless", "naked"]

        attribute topless null
        group top auto variant "a" if_any ["a"] if_not ["topless", "naked"]

        group stockings auto variant "a" if_any "a" if_not ["bottomless", "naked"]
        attribute ropes null

        attribute collar

        attribute leash if_any ["collar"]

        group multiple auto variant vibrator_a when a and (nopanties or naked)
        group multiple auto variant vibrator_b when b and (nopanties or naked)

        always "aletta_ropeplay_nohaircut" if_not ["haircut"]
        always "aletta_ropeplay_haircut" if_any ["haircut"]

        group multiple auto variant fx
        group multiple auto variant fx_a when a
        group multiple auto variant fx_b when b

    layeredimage aletta ending:
        attribute_function Pickers([HaircutPicker], npc=aletta)

        always "aletta_ending_bg"

        group base auto

        group hair auto if_any "aletta"
