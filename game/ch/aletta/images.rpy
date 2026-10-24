init 1:
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

    layeredimage aletta ending:
        attribute_function Pickers([HaircutPicker], npc=aletta)

        always "aletta_ending_bg"

        group base auto

        group hair auto if_any "aletta"
