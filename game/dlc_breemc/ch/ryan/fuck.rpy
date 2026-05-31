



















label ryan_hottub_sex_female:
    $ CONDOM = False
    show hottub sex female ryan
    "hottub sex placeholder"
    return



label ryan_sleep_date_fuck(location="hero"):
    if game.hour > 19 or game.hour < 6:
        scene bg bedroom4
        show ryan naked
        with fade
        menu:
            "You should leave":
                bree.say "I am done with you and I have to get up early tomorrow, you should leave."
                "The sex was beyond incredible."
                "Frowning a little, Ryan straightens and shrugs, then goes to collect his clothes from where he'd let it fall earlier."
                "He then heads up the stairs."
                $ ryan.love -= 1
                $ ryan.sub += 1
                call sleep from _call_sleep_113
            "You should sleep here":
                bree.say "You can stay and sleep here."
                "I say, my voice a little shaky."
                "We curl up spooning together in bed, drifting toward sleep."
                $ ryan.love += 1
                call sleep ("ryan") from _call_sleep_114
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
