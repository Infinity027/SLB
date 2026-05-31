label harmony_good_sweet_talk_female:
    show harmony
    if harmony.love > 133:
        bree.say "You're so HOT, Harmony!"
        bree.say "I can't help thinking about what I want to do to you next!"
        show harmony blush
        harmony.say "Sssh...somebody might hear you!"
        harmony.say "Whisper it to me, before I blush as red as a tomato!"
    elif harmony.love > 66:
        bree.say "I love the way you look, Harmony."
        bree.say "It shows off just how beautiful your figure really is."
        show harmony happy
        harmony.say "I...I shouldn't be proud or wanton, I know that."
        harmony.say "But it does make me happy to hear you say that!"
    else:
        bree.say "It's great to get to spend time with you away from church, Harmony."
        bree.say "It means I can get to know the real you."
        harmony.say "Aw, thank you!"
        harmony.say "I value your friendship too."
    hide harmony
    return

label harmony_bad_sweet_talk_female:
    show harmony
    bree.say "I knew you never believed in any of that religious stuff, Harmony."
    bree.say "Not really!"
    show harmony angry
    harmony.say "Hey!"
    harmony.say "Are you calling me some kind of hypocrite?"
    harmony.say "A liar?!?"
    bree.say "Ah, no...not exactly!"
    hide harmony
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
